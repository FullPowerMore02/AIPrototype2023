from flask import Flask, request, render_template
import os

# ... (import libraries ที่จำเป็น)

from tensorflow.keras.models import load_model
import numpy as np

# Load your LSTM model
model = load_model('your_lstm_model.h5')  # แก้ตามชื่อโมเดลของคุณ
scaler = MinMaxScaler()  # แก้ตามต้องการ

# ... (โค้ดอื่น ๆ ที่คุณใช้เพื่อเตรียมข้อมูล)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/upload", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # Ensure the 'uploaded_files' folder exists
        if not os.path.exists('uploaded_files'):
            os.makedirs('uploaded_files')

        namein = request.form.get('fname')
        lastnamein = request.form.get('lname')

        # Do something with the name, lastname, and file
        # (e.g., save the file, process the data, etc.)

        file = request.files['file']
        file.save(os.path.join('uploaded_files', file.filename))

        # Preprocess the data as needed
        # (e.g., read the file, scale the features, prepare the input for the LSTM)

        # Example: Scaling the features using MinMaxScaler
        data_to_predict = scaler.transform(your_preprocessed_data)

        # Reshape the data for LSTM input if needed
        # (e.g., data_to_predict = data_to_predict.reshape((1, lookback, -1)))

        # Make predictions using your LSTM model
        lstm_predictions = model.predict(data_to_predict)

        # Process the predictions as needed
        # (e.g., inverse scaling if you scaled the target variable)

        return render_template("home.html", name='Submit completed', uploaded_file=file.filename, lstm_predictions=lstm_predictions)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
