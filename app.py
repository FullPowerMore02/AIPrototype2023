from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import yfinance as yf
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('/content/lstm_model.h5')

# Function to preprocess data for prediction
def preprocess_data(df):
    df['Pct_change'] = np.log1p(df['Close'].pct_change())
    df['Log Returns'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Volatility'] = df['Log Returns'].rolling(window=20).std() * np.sqrt(252)
    df['Next_day'] = df['Close'].shift(-1)
    df.fillna(0, inplace=True)
    return df

# Function to get predictions
def get_predictions(data):
    lookback = 10
    data_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Pct_change', 'Log Returns', 'Volatility']

    X = []
    for i in range(len(data) - lookback):
        X.append(data.loc[i:i + lookback - 1, data_columns].values)

    X = np.array(X)
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X.reshape(X.shape[0], -1))
    X = X.reshape((X.shape[0], lookback, -1))

    predictions = model.predict(X)
    return predictions

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Download historical data within the specified date range
    df = yf.download('ETH-USD', start=start_date, end=end_date)

    # Preprocess the data
    df_processed = preprocess_data(df)

    # Get predictions
    predictions = get_predictions(df_processed)

    # Combine the predictions with the original data
    df_processed['Predicted_Next_day'] = np.concatenate(([np.nan] * (lookback - 1), predictions.flatten()))

    # Convert the DataFrame to HTML and pass it to the template
    table_html = df_processed.to_html(classes='table table-bordered table-hover', index=False)

    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
