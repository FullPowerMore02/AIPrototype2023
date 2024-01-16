from flask import Flask, request, render_template, make_response
import sys
import json

app = Flask(__name__)

@app.route("/name")
def helloword():
    return "Hello, World!"

@app.route("/home", methods=['POST','GET'])
def homefn():
    print ("Hello, Poro!")
    namein = request.form.get('fname')
    lastnamein = request.form.get('lname')
    print(namein)
    print(lastnamein,file=sys.stdout)
    return render_template("home.html", name=namein)



if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0", port=500
