from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/home", methods=['POST', 'GET'])
def homefn():
    if request.method == "GET":
        print('we are in home(GET)')
        name = request.args.get('fname')
        print(name)
        return render_template("home.html", name=name)
    elif request.method == "POST":
        print('we are in home(POST)')
        namein = request.form.get('fname')
        lastnamein = request.form.get('lname')
        print(namein)
        print(lastnamein)
        return render_template("home.html", name=namein)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Ensure the 'uploaded_files' folder exists
        if not os.path.exists('uploaded_files'):
            os.makedirs('uploaded_files')

        file = request.files['file']
        file.save(os.path.join('uploaded_files', file.filename))
        return render_template("home.html", name='Upload completed', uploaded_file=file.filename)

    return render_template("home.html")

if _name_ == "_main_":
    app.run(host='0.0.0.0', debug=True, port=5001)