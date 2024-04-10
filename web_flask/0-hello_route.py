 #!/usr/bin/python3
"""hello_route: First app for web python-flask"""

from flask import Flask

"""Starts a Flask web application"""

app = Flask(__name__)

"""Defines the route and returns 'Hello HBNB!'"""

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
