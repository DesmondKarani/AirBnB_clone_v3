#!/usr/bin/python3
"""Index for our web application."""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON: "status": "OK"."""
    return jsonify({"status": "OK"})
