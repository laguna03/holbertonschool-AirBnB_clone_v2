#!/usr/bin/python3
""" Start a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states/')
@app.route('/states/<id>')
def states_and_state(id=None):
    """ Display list of all the states """
    if id:
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)