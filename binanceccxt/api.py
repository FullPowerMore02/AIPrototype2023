# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime,timedelta
from flask import Flask,render_template, jsonify
from tensorflow.keras.models import load_model
import joblib
from flask_cors import CORS
import plotly.express as px
import os
import ccxt
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

model_path = 'eth_lstm_model.h5'
scaler_path = 'eth_scaler.pkl'


print(model_path)
time_steps = 20 

model = load_model(model_path) # LSTM
scaler = joblib.load(scaler_path) # scaler MinMaxScaler


ETH_data = ccxt.binance().fetch_ohlcv('ETH/USDT', timeframe='1d')
df = pd.DataFrame(ETH_data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date'] = pd.to_datetime(df['Date'], unit='ms')
df['Date'] = df['Date'].dt.date
df.set_index('Date', inplace=True)
data = df.filter(['Close'])




last_results = pd.DataFrame({'close': data.values.reshape(-1, )}, index=data.index)
last_results['close'] = scaler.transform(last_results['close'].values.reshape(-1, 1))
start_date = data.index[-1]
         


app = Flask(__name__, template_folder='template')  # still relative to module
CORS(app)






# LSTM
def predict_values_for_future_dates(model, data, start_date, num_dates, time_steps):
    predictions = []

    current_date = datetime.combine(start_date, datetime.min.time())
    
    for _ in range(num_dates):
        input_data = data[-time_steps:].values
        input_data = input_data.reshape(1, time_steps, 1)
        
        prediction = model.predict(input_data)
        predictions.append(prediction[0, 0])
        
        current_date += timedelta(days=1)
        
        data = pd.concat([data, pd.DataFrame({'close': prediction[0, 0]}, index=[current_date])])

    return predictions


@app.route('/')
def home():
    return render_template('index.html')





# (num_dates)
@app.route('/forecast/<int:num_dates>', methods=['GET'])
def forecast(num_dates):
    try:
        # calculate  (USD $)
        predicted_values = predict_values_for_future_dates(model, last_results, start_date, int(num_dates)+1, time_steps)
        print(predicted_values)
        NEW_DATES = [start_date]
        for _ in range(num_dates):
            data_append = datetime.date(data.index[-1] + pd.DateOffset(days=_+1))
            NEW_DATES.append(data_append)
        RESULTS = pd.DataFrame({'close': predicted_values[:]}, index=NEW_DATES)
        RESULTS['close'] = scaler.inverse_transform(RESULTS[['close']])
        predictions = RESULTS['close']
        date_value_pairs = {}
        for date, prediction in zip(RESULTS.index, predictions):
            date_value_pairs[str(date)] = prediction
        date_value_pairs.pop(next(iter(date_value_pairs))) # (start_date)
        forecast_data = {
            'num_dates': date_value_pairs
            }
        fig = px.line(RESULTS, x=RESULTS.index, y='close')
        fig.update_xaxes(title_text='DATA')
        fig.update_yaxes(title_text='VALUE IN USD$')

        forecast_data['graph'] = fig.to_json() # 'forecast'

        return jsonify(forecast_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 400



if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
