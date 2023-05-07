#!/usr/bin/python3
"""start a web flask application"""


from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def stat():
    """defining the function """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def closedown(exc):
    """defining the function"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
