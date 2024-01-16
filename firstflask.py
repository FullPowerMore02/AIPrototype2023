from flask import Flask, request, render_template, make_response
import sys
import json

app = Flask(__name__)

##API
@app.route("/request",methods=['POST'])
def web_service_API ():
    payload = request.data.decode("url-8")
    inmessage = json.loads(payload)
    print(inmessage)

    json_data = json.dumps({'y':'received!'})
    return json_data
    
@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/home", methods=['POST','GET'])
def homefn():
    if request.method == "GET":
       print('we are in home(GET)', file=sys.stdout)
       name = request.args.get('fname')
       print(name, file=sys.stdout)
       return render_template("home.html",name=name)
        #getting input with name = fname in HTML form
    elif request.method == "POST":
       print('we are in home(POST)', file=sys.stdout)
       namein = request.form.get('fname')
       lastnamein = request.form.get('lname')
       print(namein, file=sys.stdout)
       print(lastnamein, file=sys.stdout)
       return render_template("home.html",name=namein)

####



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('file')
        return render_template("home.html",name='upload completed')
    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
