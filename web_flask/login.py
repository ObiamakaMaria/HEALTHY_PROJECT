#!/usr/bin/env python3

from flask import Blueprint, render_template, request, jsonify

# Define the blueprint
login_bp = Blueprint('login', __name__)

# Route to handle login POST requests
@login_bp.route('/login', methods=['POST'])
def login():
    # Get the username and password from the POST request
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Check the username and password and perform your logic here
    # For example, you could authenticate the user and return a response
    response =  {
            'message' : "recived your request",
            'data': username
            }
    
    # Render a webpage as a response (replace 'login.html' with your actual HTML template)
    return jsonify(response)

