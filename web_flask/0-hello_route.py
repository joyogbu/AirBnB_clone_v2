#!/usr/bin/python3
""" python script that starts a flaskweb application """


from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
	return ("Hello HBNB!")

if __name__ == '(__main__)':
	#export FLASK_APP=0-hello_route
	#flask run
	app.run(host="0.0.0.0", port=5000)
