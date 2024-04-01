#!/usr/bin/python3
"""This module starts a Flask web application."""
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
# Setup CORS to allow all origins for all routes
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Custom 404 Not Found error handler."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
