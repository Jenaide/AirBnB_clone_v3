#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jenaide Sibolie
"""
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)
CORS(app_views)


@app.teardown_appcontext
def teardown_db(error):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """handler for 404 errors that returns a JSON-formatted
    404 status code response.
    """
    return ({'error': 'Not found'}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
