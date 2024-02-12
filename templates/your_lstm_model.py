import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
%matplotlib inline
import os
import shap
import yfinance as yf
from sklearn.model_selection import TimeSeriesSplit
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from keras.layers import Bidirectional
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error
import shap
tf.compat.v1.disable_v2_behavior()
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
df = pd.read_csv("data01.csv")
new_column_names = {
    'date': 'Date',
    'eth-usd_Open': 'Open',
    'eth-usd_High': 'High',
    'eth-usd_Low': 'Low',
    'eth-usd_Close': 'Close',
    'eth-usd_Adj Close': 'Adj Close',
    'eth-usd_Volume': 'Volume'
}
df.rename(columns=new_column_names, inplace=True)
df.set_index('Date', inplace=True)
df['Pct_change'] = df['Close'].pct_change()
df['Pct_change'] = np.log1p(df['Pct_change'])
short_period = 12  # Short-term EMA period
long_period = 26  # Long-term EMA period
signal_period = 9  # Signal line EMA period
df['Log Returns'] = np.log(df['Close'] / df['Close'].shift(1))
df['Volatility'] = df['Log Returns'].rolling(window=20).std() * np.sqrt(252)
df['Next_day'] = df['Close'].shift(-1)
df = df.dropna()
scaler = MinMaxScaler()
scale_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'btc-usd_Open',
       'btc-usd_High', 'btc-usd_Low', 'btc-usd_Close', 'btc-usd_Adj Close',
       'btc-usd_Volume', 'cl=f_Open', 'cl=f_High', 'cl=f_Low', 'cl=f_Close',
       'cl=f_Adj Close', 'cl=f_Volume', '^dji_Open', '^dji_High', '^dji_Low',
       '^dji_Close', '^dji_Adj Close', '^dji_Volume', '^gspc_Open',
       '^gspc_High', '^gspc_Low', '^gspc_Close', '^gspc_Adj Close',
       '^gspc_Volume', '^ixic_Open', '^ixic_High', '^ixic_Low', '^ixic_Close',
       '^ixic_Adj Close', '^ixic_Volume', '^n225_Open', '^n225_High',
       '^n225_Low', '^n225_Close', '^n225_Adj Close', '^n225_Volume',
       'day_sentiment', 'day_n_views', 'day_n_shares', 'FEDFUNDS',
       'Pct_change', 'Log Returns', 'Volatility',  'Next_day']

scaled_df = scaler.fit_transform(df[scale_cols])
scaled_df = pd.DataFrame(scaled_df, columns=scale_cols)
print(scaled_df)
features  = df.columns[:-1]
lookback = 10 
data_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'btc-usd_Open',
       'btc-usd_High', 'btc-usd_Low', 'btc-usd_Close', 'btc-usd_Adj Close',
       'btc-usd_Volume', 'cl=f_Open', 'cl=f_High', 'cl=f_Low', 'cl=f_Close',
       'cl=f_Adj Close', 'cl=f_Volume', '^dji_Open', '^dji_High', '^dji_Low',
       '^dji_Close', '^dji_Adj Close', '^dji_Volume', '^gspc_Open',
       '^gspc_High', '^gspc_Low', '^gspc_Close', '^gspc_Adj Close',
       '^gspc_Volume', '^ixic_Open', '^ixic_High', '^ixic_Low', '^ixic_Close',
       '^ixic_Adj Close', '^ixic_Volume', '^n225_Open', '^n225_High',
       '^n225_Low', '^n225_Close', '^n225_Adj Close', '^n225_Volume',
       'day_sentiment', 'day_n_views', 'day_n_shares', 'FEDFUNDS',
       'Pct_change', 'Log Returns', 'Volatility']
target_columns = ['Next_day']
df_reset = df.reset_index(drop=True)
X = []
y = []
for i in range(len(df_reset) - lookback):
    X.append(df_reset.loc[i:i+lookback-1, data_columns].values)  # to select only the columns specified in data_columns
    y.append(df_reset.loc[i+lookback, target_columns].values[0])  # select the target value
X = np.array(X)
y = np.array(y)
scaler = MinMaxScaler()
X = scaler.fit_transform(X.reshape(X.shape[0], -1))
y_scaler = MinMaxScaler()
y = y_scaler.fit_transform(y.reshape(-1, 1))
tscv = TimeSeriesSplit(gap=0, max_train_size=None, n_splits=20, test_size=64)
for train_index, test_index in tscv.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
X_train = X_train.reshape((X_train.shape[0], lookback, -1))
X_test = X_test.reshape((X_test.shape[0], lookback, -1))
def build_single_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(256, return_sequences=False, input_shape= input_shape))
    model.add(Dense(50))
    model.add(Dense(1))
    model.compile(optimizer='RMSprop', loss='mean_squared_error')
    return model
input_shape = (X_train.shape[1], X_train.shape[2])
single_lstm_model = build_single_lstm_model(input_shape)
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=100, mode='min')
single_history = single_lstm_model.fit(X_train, y_train, epochs=100, batch_size=64,
                    validation_data=(X_test, y_test), callbacks=[early_stopping])
single_lstm_model.summary()
single_pred = single_lstm_model.predict(X_test)
plt.figure(figsize=(12, 6))
plt.title('Single-Layered-LSTM, window_size=10')
plt.ylabel('close price')
plt.xlabel('period')
plt.plot(y_test, label='actual')
plt.plot(single_pred, label='prediction')
plt.grid()
plt.legend(loc='best')
plt.show()
y_single_pred_original = y_scaler.inverse_transform(single_pred)
y_single_test_original = y_scaler.inverse_transform(y_test)
df_reset = df.reset_index()
real_rmse_single = np.sqrt(mean_squared_error(y_single_test_original, y_single_pred_original))
real_mae_single = mean_absolute_error(y_single_test_original, y_single_pred_original)
real_mape_single = mean_absolute_percentage_error(y_single_test_original, y_single_pred_original)
print("RMSE of Single-Layered-LSTM :", real_rmse_single)
print("MAE of Single-Layered-LSTM :", real_mae_single)
print("MAPE of Single-Layered-LSTM :", real_mape_single)
plt.figure(figsize=(5, 5))
plt.plot(single_history.history['loss'])
plt.plot(single_history.history['val_loss'])
plt.title('Training Loss vs. Validation Loss of Single-LSTM')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training Loss', 'Validation Loss'], loc='upper right')
plt.show()