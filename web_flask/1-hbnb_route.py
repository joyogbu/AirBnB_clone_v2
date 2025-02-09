#!/usr/bin/python3
""" python script that starts a flaskweb application """


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """defining hello_hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hnb2():
    """defining hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
