#!/usr/bin/python3
""" python script that starts a flaskweb application """


from web_flask import app


@app.route("/", strict_slashes=False)
def hello_hbnb():
	return "Hello HBNB!"

if __name__ == "__main__":
	app.run(host="0.0.0.0")
