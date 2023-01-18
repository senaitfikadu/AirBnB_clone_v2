#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(name)


@app.route('/states')
@app.route('/states/<id>')
def state_filter(id=None):
    """Render template with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session"""
    storage.close()


if name == 'main':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
