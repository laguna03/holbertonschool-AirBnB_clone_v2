 #!/usr/bin/python3

from flask import Flask

'''Starts a Flask web application'''

app = Flask(__name__)

'''Defines the route '/' and returns "Hello HBNB!"'''

@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''Displays Hello HBNB!'''
    return 'Hello HBNB!'

'''Defines the route '/hbnb' and returns "HBNB"'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
