#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/')
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'])
def unauthorized() -> str:
    """GET /api/v1/unauthorized
    Return: error msg"""
    abort(401)


@app_views.route('forbidden')
def forbidden() -> str:
    """GET /api/v1/forbidden
    Return: forbidden err"""
    abort(403)
