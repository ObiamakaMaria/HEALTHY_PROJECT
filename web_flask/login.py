#!/usr/bin/env python3

""" This is the module for handling user login request"""

from flask import Blueprint, render_template, request, jsonify, send_from_directory, session
from models import storage
from models.user import User
from werkzeug.security import check_password_hash
# Define the blueprint
login_bp = Blueprint('login', __name__)

# Route to handle login POST requests
@login_bp.route('/login', endpoint='login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return send_from_directory('servee_app', 'login.html')
    # Get the username and password from the POST request
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Perform input validation
    if not (username and password):
        return jsonify({'error': 'Username, password'}), 400

    # Check for SQL injection
    if any([';' in username, ';' in password]):
        return jsonify({'error': 'Input contains potentially malicious characters'}), 400


    # Check if the password or username exists
    user_data = storage.all(User)
    for key in user_data:
        if user_data[key].username.lower() == username.lower():
            if check_password_hash(user_data[key].password_hash, password):
               session['user_id'] = user_data[key].id
               return jsonify({'success':user_data[key].id}), 200
    response =  {
            'message' : "Password or username incorrect"
            }

    return jsonify(response), 400

