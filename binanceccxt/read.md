# ETH Flask LSTM Price Prediction
http://20.198.93.92:5001/
This repository contains an implementation of a ETH Price Prediction system using LSTM (Long Short-Term Memory) neural networks. The system utilizes the CCXT library for fetching historical stock price data, Flask for building a RESTful API, and TensorFlow for implementing the LSTM model. Additionally, it includes components written in JavaScript, HTML, and CSS for the frontend interface.

## Library Used
- TensorFlow
- Flask
- CCXT
- JavaScript
- HTML
- CSS


## How to Use
### Windows
1. Open your command prompt.
2. Navigate to the project directory.
3. Run the following command:
    ```
    rm -rf eth_lstm_model.h5
    rm -rf eth_scaler.pkl
    python model_explorer.py
    python api.py
    ```

### macOS
1. Open your terminal.
2. Navigate to the project directory.
3. Run the following command:
    ```
    rm -rf eth_lstm_model.h5
    rm -rf eth_scaler.pkl
    python3 model_explorer.py
    python3 api.py
    ```
