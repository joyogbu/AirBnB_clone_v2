#!/usr/bin/python3
""" python script that starts a flaskweb application """


from flask import Flask


app = Flask(__name__)


@app.route("/airbnb-onepage", strict_slashes=False)
def hello_hbnb():
    """defining the finction"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
