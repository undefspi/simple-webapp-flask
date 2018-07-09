import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the docker version of the openshift test!"

@app.route('/how are you')
def hello():
    return 'I am building images from a docker file and into openshift?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
