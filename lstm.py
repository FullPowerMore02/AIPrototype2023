from flask import Flask, render_template
import yfinance as yf
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
from sklearn.model_selection import TimeSeriesSplit

app = Flask(__name__)

# โหลดโมเดลที่ถูกฝึกสอนไว้
model = tf.keras.models.load_model('lstm_model.h5')

# กำหนดตัวแปร date_values_bi ให้เป็น global
date_values_bi = None

# โค้ดเตรียมข้อมูลของคุณ
df = yf.download('ETH-USD')
df['Pct_change'] = np.log1p(df['Close'].pct_change())
df['Log Returns'] = np.log(df['Close'] / df['Close'].shift(1))
df['Volatility'] = df['Log Returns'].rolling(window=20).std() * np.sqrt(252)
df['Next_day'] = df['Close'].shift(-1)
df.fillna(0, inplace=True)

# เลือกข้อมูลที่ต้องการใช้
data_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Pct_change', 'Log Returns', 'Volatility']
target_columns = ['Next_day']

# เลือกข้อมูลเฉพาะตัวแปรที่ใช้ในการทำนาย
df_selected = df[data_columns + target_columns].copy()

# คำนวณค่า Percentage Change และ Log Returns
df_selected['Pct_change'] = np.log1p(df_selected['Close'].pct_change())
df_selected['Log Returns'] = np.log(df_selected['Close'] / df_selected['Close'].shift(1))

# คำนวณค่า Volatility
df_selected['Volatility'] = df_selected['Log Returns'].rolling(window=20).std() * np.sqrt(252)

# กรองข้อมูลที่ไม่มีค่า NaN
df_selected.dropna(inplace=True)

# กำหนดขนาดของหน้าต่างเวลา (lookback)
lookback = 10

# กำหนดตัวแปรที่ใช้ในการทำนาย
X = []
y = []

# สร้างข้อมูลสำหรับการทำนาย
for i in range(len(df_selected) - lookback):
    X.append(df_selected.iloc[i:i+lookback, df_selected.columns.isin(data_columns)].values)
    y.append(df_selected.iloc[i+lookback, df_selected.columns.isin(target_columns)].values[0])

X = np.array(X)
y = np.array(y)

# ปรับค่าข้อมูลให้อยู่ในช่วง 0-1
scaler = MinMaxScaler()
X = scaler.fit_transform(X.reshape(X.shape[0], -1))
y_scaler = MinMaxScaler()
y = y_scaler.fit_transform(y.reshape(-1, 1))

X = X.reshape((X.shape[0], lookback, -1))

# สร้างข้อมูลทดสอบและฝึกอบรม
tscv = TimeSeriesSplit(gap=0, max_train_size=None, n_splits=20, test_size=64)
for train_index, test_index in tscv.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

X_train = X_train.reshape((X_train.shape[0], lookback, -1))
X_test = X_test.reshape((X_test.shape[0], lookback, -1))

# สร้างข้อมูลใหม่สำหรับทำนาย
new_data_point = [X_test[-1] + 0.002, X_test[-1] + 0.00145, X_test[-1] + 0.006475, X_test[-1] + 0.00893]
X_test_appended = np.append(X_test, new_data_point, axis=0)

# เส้นทางสำหรับการแสดงผลการทำนายราคาหุ้น
@app.route('/')
def stock_predictions():
    global date_values_bi  # ประกาศให้ date_values_bi เป็น global

    # ทำนาย
    s_pred = model.predict(X_test)
    s_plus_pred = model.predict(X_test_appended)

    y_s_pred = y_scaler.inverse_transform(s_pred)
    y_s_plus_pred = y_scaler.inverse_transform(s_plus_pred)
    y_y_test = y_scaler.inverse_transform(y_test)

    # กำหนดรูปแบบของวันที่
    df_reset = df.reset_index()
    date_values_bi = df_reset['Date'].iloc[test_index].values
    date_values_bi = [date[:10] for date in date_values_bi.astype('str')]
    date_values_bi = np.array(date_values_bi)
    start_date = datetime.strptime(date_values_bi[-1], '%Y-%m-%d')
    date_values_list_pred = [start_date + timedelta(days=i) for i in range(1, 5)]
    date_values_list_pred = [date.strftime('%Y-%m-%d') for date in date_values_list_pred]
    date_values_bi_pred = np.append(date_values_bi, date_values_list_pred)

    # เตรียมข้อมูลสำหรับแสดงผล
    data = {
        'date_values_actual': date_values_bi[:-1],
        'y_test_actual': y_y_test[:-1].tolist(),
        'date_values_pred': date_values_bi_pred,
        'y_pred': y_s_plus_pred.tolist(),
        'last_actual_date': date_values_bi[-2]
    }

    return render_template('stock_predictions.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
