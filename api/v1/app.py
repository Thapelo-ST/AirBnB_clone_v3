#!/usr/bin/python3
"""
    creates flask app(HBNB) and registers the
    BluePrint app_views with flask instance HBNB
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = flask(__name__)

# allow request from any origin and enable cors
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})

# register app_views blueprint
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


# teardown function for SQLAlchemy close session after each request
@app.teardown_appcontext
def engine_teardown(exception):
    """
        delete current SQLAlchemy session obj after each request
    """
    storage.close()


# Errot handling
@app.errorhandler(404)
def not_found(error):
    """
        return "not found" erorr message from json response
    """
    response = {'error': 'Not found'}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_HOST', '5000'))
    app.run(host=HOST, port=PORT, threaded=True)
