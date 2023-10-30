#!/usr/bin/python3
"""make a route /status on obj app_views"""

from flask import jsonify
from api.v1.view import app_view
from models import storage


@app_views.route('/status', method=['GET'])
def api_status():
    """returns json for RestFul API status"""
    resp = {'status': 'OK'}
    return jsonify(resp)


# Task Number 4
@app_views.route('/stats', methods=['GET'])
def get_stats():
    """gets number of objects in each of the type"""
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('Users')
            }
    return jsonify(stats)
