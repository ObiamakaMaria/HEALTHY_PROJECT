#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, send_from_directory
from models import storage
from models.user import User  # Import your DBStorage class
import re
from werkzeug.security import generate_password_hash
from sqlalchemy import func


# Define the blueprint
register_bp = Blueprint('register', __name__)

# Initialize DBStorage instance

# Route to handle register POST requests
@register_bp.route('/register', endpoint='register', methods=['POST', 'GET'])
def register():
    
    #the get method first, then elif for the post method
    if request.method == 'GET':
        return send_from_directory('static', 'signup.html')
    elif request.method == 'POST':
        #get the user input from he request module
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')

        email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
        #hash the password
        hashed_password = generate_password_hash(password)

        def is_valid_email(email):
            """ function that checks if email is valid"""
            return re.match(email_pattern, email) is not None

        # Perform input validation
        if not (username and password and email):
            return jsonify({'error': 'Username, password, and email are required'}), 400

        # Check for SQL injection
        if any([';' in username, ';' in password, ';' in email]):
            return jsonify({'error': 'Input contains potentially malicious characters'}), 400

        # check if the email is valid
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        # Check if the email or username already exists in the database
        user_data = storage.all(User)
        for key in user_data:
            if user_data[key].email.lower() == email.lower():
                return jsonify({'error': 'Email already exists. please use a different email.'}), 400
            elif user_data[key].username.lower() == username.lower():
                return jsonify({'error': 'Username already exists. Please choose a different username.'}), 400

        #save new user to the database        
        new_user = User(username=username.lower(), email=email.lower(), password_hash=hashed_password)
        new_user.save()
        response = {
            'message': "You have been registered successfully",
            'data': {'username': username, 'email': email}
        }
        return jsonify(response), 200

