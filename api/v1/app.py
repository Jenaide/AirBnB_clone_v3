#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(error):
    """closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,
            threaded=True, debug=True)
