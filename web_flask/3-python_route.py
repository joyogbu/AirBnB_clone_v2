#!/usr/bin/python3
""" python script that starts a flaskweb application """


from flask import Flask
from flask import escape

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""defining hello_hbnb"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hnb2():	
	"""defining hbnb"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hello3(text='is cool'):
	"""define the function"""
	return "C %s" % escape(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello4(text):
	"""defining the function"""
	return "Python %s" % escape(text.replace('_', ' '))
	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
