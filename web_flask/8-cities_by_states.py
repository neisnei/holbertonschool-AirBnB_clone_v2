#!/usr/bin/python3

"""
Module script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.route('cities_by_states', strict_slashes=False)
def cities_by_states():
    city_li = storage.all(State).values()
    return render_template('8-cities_by_states.html', cities=city_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
