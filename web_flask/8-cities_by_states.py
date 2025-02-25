#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route taht displays the html page of
    a list of states objects sorted by name
    """
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Route that displays a HTML page with a list of cities
    objects sorted by name """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html',
            states=states, cities=cities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
