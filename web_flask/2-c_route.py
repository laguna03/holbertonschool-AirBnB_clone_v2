#!usr/bin/python3
"""c_route: First app for web python-flask"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Say Hello"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Say HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Say C"""
    return 'C %s' % text.replace('_', ' ')
