#!/usr/bin/python3
"""
Starts a Flask web app
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    return render_template(
        "cities_by_states.html", states=states, strict_slashes=False
    )


@app.teardown_appcontext
def close_session(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
