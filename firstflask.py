from flask import Flask, request, render_template, make_response

import json

app = Flask(__name__) :
# @ อ่านว่า รูท
@app.route("/")
def helloworld():
    return "Hello, World"

if __name__ == "__main__"
### 0.0.0.0 ให้เครื่องอื่นเห็นได้
    app.run(host='0.0.0.0',debug=True,post=5001)####