#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask
from urllib.parse import unquote_plus

""" Create new Flask instance"""
app = Flask(__name__)

""" Define principal route ("/") with msg "Hello HBNB!" """

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

""" Define route ("/hbnb") with msg "HBNB" """

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

""" Define route ("/c/<text>") with msg "C <text>" """

@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    tetx = unquote_plus(text.replace('_', ' '))
    return (f"C {text}")

""" Define route ("/python/") with msg "Python is cool" """

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    text = unquote_plus(text.replace('_', ' '))
    return (f"Python {text}")


""" Configure app to listen in 0.0.0.0 in port 5000 """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

