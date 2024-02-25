# app.py
from flask import Flask, render_template
import yfinance as yf
from model import load_lstm_model, preprocess_data, prepare_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

def generate_plot():
    df = yf.download('^GSPC', start='2012-01-01', end='2022-12-31')
    df['Pct_change'] = df['Close'].pct_change()
    df['Pct_change'] = np.log1p(df['Pct_change'])
    df['Log Returns'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Volatility'] = df['Log Returns'].rolling(window=20).std() * np.sqrt(252)
    df['Next_day'] = df['Close'].shift(-1)
    df = df.dropna()

    scaled_df = preprocess_data(df)

    lookback = 10
    X, y = prepare_data(scaled_df, lookback)

    # Split data into train and test sets
    tscv = TimeSeriesSplit(gap=0, max_train_size=None, n_splits=20, test_size=64)
    train_index, test_index = next(tscv.split(X, y))
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    X_train = X_train.reshape((X_train.shape[0], lookback, -1))
    X_test = X_test.reshape((X_test.shape[0], lookback, -1))

    loaded_model = load_lstm_model()

    df_reset = df.reset_index()
    date_values_bi = df_reset['Date'].iloc[test_index].values
    date_values_bi = date_values_bi.astype('str')

    # Assume you have some testing data
    new_data_point = X_test[-1] + 0.002
    X_test_appended = np.append(X_test, [new_data_point], axis=0)
    predictions = loaded_model.predict(X_test_appended)

    y_scaler = MinMaxScaler()
    y_single_pred_original = y_scaler.inverse_transform(predictions)
    y_single_test_original = y_scaler.inverse_transform(y_test)

    plt.figure(figsize=(12, 6))
    plt.title('Single-Layered-LSTM, window_size=10')
    plt.ylabel('close price')
    plt.xlabel('period')
    plt.plot(y_single_test_original, label='actual')
    plt.plot(y_single_pred_original, label='prediction')
    plt.axvline(64, color='red')
    plt.grid()
    plt.legend(loc='best')

    # Save the plot to BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Encode the image as base64
    plot_data = base64.b64encode(buf.read()).decode('utf-8')

    return render_template('index.html', plot_data=plot_data)

@app.route('/')
def index():
    plot_data = generate_plot()
    return render_template('index.html', plot_data=plot_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)

