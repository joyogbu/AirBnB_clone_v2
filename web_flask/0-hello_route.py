#!/usr/bin/python3
""" python script that starts a flaskweb application """

from web_flask import app
#from flask import Flask
#app = Flask('web_flask')

@app.route("/", strict_slashes=False)
def hello_hbnb():
	return "Hello HBNB!"

if __name__ == "__main__":
	#export FLASK_APP=0-hello_route
	#flask run
	app.run(host="0.0.0.0")
	#app.run()
