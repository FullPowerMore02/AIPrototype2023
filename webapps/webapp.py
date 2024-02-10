from flask import Flask, render_template, request
from your_ml_module import load_lstm_model, preprocess_data  # นำเข้าฟังก์ชันที่จำเป็น

app = Flask(__name__)
lstm_model = load_lstm_model()  # โหลดโมเดลที่คุณสร้าง

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # ตรวจสอบว่ามีไฟล์ถูกอัพโหลดหรือไม่
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']

        # ตรวจสอบว่าไฟล์ไม่ว่าง
        if file.filename == '':
            return "No selected file"

        # ทำนายด้วยโมเดล LSTM
        input_data = preprocess_data(file)  # ทำการประมวลผลไฟล์

        prediction = lstm_model.predict(input_data)

        # ส่งผลลัพธ์ไปที่หน้าเว็บ
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
