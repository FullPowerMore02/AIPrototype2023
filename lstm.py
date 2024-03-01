
### Stock_Prediction for Youtube Video 
### Date Created: 02/19/2024
### Author: Vivian Aranha

from flask import Flask, request, jsonify
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Function to fetch and preprocess the stock data
def fetch_and_preprocess_stock_data(symbol):
    # Download historical data
    stock_data = yf.download(symbol, start='2010-01-01', end='2024-02-18')

    # Drop rows with missing values
    stock_data_cleaned = stock_data.dropna()

    return stock_data_cleaned

# Load and preprocess the dataset
stock_data_cleaned = fetch_and_preprocess_stock_data('AAPL')  # Replace 'AAPL' with your desired stock symbol

# Define features (X) and target variable (y)
X = stock_data_cleaned[['Open', 'High', 'Low', 'Volume']]  # Adjust features as needed
y = stock_data_cleaned['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Define a route for receiving stock symbol and returning predicted price
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    stock_features = data['features']  # Assuming the features are passed in a JSON format
    predicted_price = model.predict([stock_features])[0]
    response = {'predicted_price': predicted_price}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
