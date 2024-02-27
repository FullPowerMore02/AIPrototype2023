from flask import Flask, render_template, send_file
import yfinance as yf
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    # ดาวน์โหลดข้อมูล
    df = yf.download('ETH-USD')

    # คำนวณและเพิ่มคอลัมน์
    df['Pct_change'] = np.log1p(df['Close'].pct_change())
    df['Log Returns'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Volatility'] = df['Log Returns'].rolling(window=20).std() * np.sqrt(252)
    df['Next_day'] = df['Close'].shift(-1)
    df.fillna(0, inplace=True)

    # ระบุคอลัมน์ที่ต้องการบันทึก
    data_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Pct_change', 'Log Returns', 'Volatility']
    target_columns = ['Next_day']

    # บันทึกลงในไฟล์ CSV
    df.to_csv('ethereum_data.csv', columns=data_columns + target_columns)

    return render_template('index.html', filename='ethereum_data.csv')

@app.route('/download')
def download():
    return send_file('ethereum_data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
