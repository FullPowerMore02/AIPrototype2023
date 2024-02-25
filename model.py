# model.py
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import TimeSeriesSplit
import yfinance as yf

tf.compat.v1.disable_v2_behavior()

def build_single_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(256, return_sequences=False, input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='Adam', loss='mean_squared_error')
    return model

def train_lstm_model(X_train, y_train, X_test, y_test):
    input_shape = (X_train.shape[1], X_train.shape[2])
    single_lstm_model = build_single_lstm_model(input_shape)
    
    early_stopping = EarlyStopping(monitor='val_loss', patience=100, mode='min')
    
    single_history = single_lstm_model.fit(X_train, y_train, epochs=50, batch_size=64,
                                           validation_data=(X_test, y_test), callbacks=[early_stopping])
    
    single_lstm_model.save("lstm_model")
    
    return single_lstm_model

def load_lstm_model():
    loaded_model = tf.keras.models.load_model("lstm_model")
    return loaded_model

def preprocess_data(df):
    scaler = MinMaxScaler()
    scale_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume',
                  'Pct_change', 'Log Returns', 'Volatility', 'Next_day']
    scaled_df = scaler.fit_transform(df[scale_cols])
    scaled_df = pd.DataFrame(scaled_df, columns=scale_cols)
    return scaled_df

def prepare_data(df, lookback):
    data_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume',
                    'Pct_change', 'Log Returns', 'Volatility']
    target_columns = ['Next_day']
    
    X = []
    y = []

    for i in range(len(df) - lookback):
        X.append(df.loc[i:i+lookback-1, data_columns].values)
        y.append(df.loc[i+lookback, target_columns].values[0])

    X = np.array(X)
    y = np.array(y)
    
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X.reshape(X.shape[0], -1))
    
    y_scaler = MinMaxScaler()
    y = y_scaler.fit_transform(y.reshape(-1, 1))
    
    return X, y
