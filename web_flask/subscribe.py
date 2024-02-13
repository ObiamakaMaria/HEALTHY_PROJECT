#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, send_from_directory
from models import storage
from models.user import User  # Import your DBStorage class
import re
from sqlalchemy import func
from web_flask.decorator import require_login


# Define the blueprint
subscribe_bp = Blueprint('subscribe', __name__)

# Initialize DBStorage instance

# Route to handle register POST requests
@subscribe_bp.route('/subscribe', endpoint='subscribe', methods=['POST', 'GET'])
@require_login
def subscribe():

    #the get method first, then elif for the post method
    if request.method == 'GET':
        return send_from_directory('static', 'subscribe.html')
