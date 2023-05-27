#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/vi')

if (__name__ == 'api.v1.views'):
    from api.v1.views.index import *
