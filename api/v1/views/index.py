#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage



@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Checks status of the routes"""
    return jsonify({'status': 'OK'})

@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    stats = {"amenities": 'Amenity', "cities": 'City', "places": 'Place',
              "reviews": 'Review', "states": 'State', "users": 'User'}
    for key, value in stats.items():
        stats[key] = storage.count(value)
    return jsonify({stats})
