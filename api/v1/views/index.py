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


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON: 'status': 'OK'."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each object by type."""
    # Dictionary mapping class names to their corresponding model classes
    class_dict = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }

    # Count the number of instances for each model class
    counts = {cls_key: storage.count(cls_val) for cls_key,
              cls_val in class_dict.items()}
    return jsonify(counts)
