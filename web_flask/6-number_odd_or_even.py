#!/usr/bin/python3
""" python script that starts a flaskweb application """


from flask import Flask
from flask import escape
from flask import render_template

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
def hello3(text):
	"""define the function"""
	return "C %s" % escape(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello4(text='is_cool'):
	"""defining the function"""
	return "Python %s" % escape(text.replace('_', ' '))

@app.route("/number/<int:n>", strict_slashes=False)
def number1(n):
	"""defining the function"""
	if type(n) == int:
		return ("{} is a number".format(n))

@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
	"""defining the function"""
	if type(n) == int:
		return render_template('5-number.html', nu=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number2(n):
	"""defining the function"""
	out = ""
	if type(n) == int:
		if (n % 2) == 0:
			out = "even"
		else:
			out = "odd"
		return render_template('6-number_odd_or_even.html', nu=n, text=out)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
