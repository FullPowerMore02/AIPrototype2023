from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'

    # ทำอย่างอื่น ๆ ที่ต้องการกับไฟล์ที่อัพโหลด
    # ตัวอย่าง: file.save('uploads/' + file.filename)

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
