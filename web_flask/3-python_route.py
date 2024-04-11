#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask
from urllib.parse import unquote_plus

""" Create new Flask instance"""
app = Flask(__name__)

""" Define principal route ("/") with msg "Hello HBNB!" """

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    tetx = unquote_plus(text.replace('_', ' '))
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
        text = unquote_plus(text.replace('_', ' '))
        return (f"Python {text}")



if __name__ == '__main__':
    """ Configure app to listen in 0.0.0.0 in port 5000 """

app.run(host='0.0.0.0', port=5000)

