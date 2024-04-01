#!/usr/bin/python3
"""Index for our web application."""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


# Assuming these are all the classes you want to count
classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON: 'status': 'OK'."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each object by type."""
    counts = {cls: storage.count(eval("models." +
                                      classes[cls])) for cls in classes}
    return jsonify(counts)
