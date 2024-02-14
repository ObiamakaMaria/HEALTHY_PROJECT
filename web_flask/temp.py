#!/usr/bin/env python3

from flask import Blueprint, render_template, request, jsonify, send_from_directory
from models import storage
from models.user import User
from werkzeug.security import check_password_hash
from web_flask.decorator import require_login
# Define the blueprint
temp_bp = Blueprint('temp', __name__)

# Route to handle login POST requests
@temp_bp.route('/temp', endpoint='temp', methods=['GET'])
@require_login
def temp():
    return send_from_directory('static', 'subscribe.html')

