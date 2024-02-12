from flask import Flask, request, render_template
import os

app = Flask(__name__)

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

        return render_template("home.html", name='Submit completed', uploaded_file=file.filename)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
