#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Checks status of the routes"""
    return jsonify({'status': 'OK'})
