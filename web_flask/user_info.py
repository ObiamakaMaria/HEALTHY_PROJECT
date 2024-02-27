#!/usr/bin/env python3

""" This module handle get request for user email and name to display on profiel """


from flask import Blueprint, request, jsonify, session
from models import storage
from models.user import User
# Define the blueprint
info_bp = Blueprint('info', __name__)

# Route to handle login POST requests
@info_bp.route('/info', endpoint='info')
def info():


    # Check if user is logged in
    user_data = storage.all(User)
    for key in user_data:
        if user_data[key].id  == session['user_id']:
               return jsonify({'name':user_data[key].username, 'email' : user_data[key].email}), 200
    response =  {
            'message' : "You are not  authorized to make this request"
            }

    return jsonify(response), 400
