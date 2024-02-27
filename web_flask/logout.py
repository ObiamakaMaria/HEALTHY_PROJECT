#!/usr/bin/env python3

""" This is the module that handles user logout request """

from flask import Blueprint, request, jsonify, session, redirect, url_for

# Define the blueprint
logout_bp = Blueprint('logout', __name__)

# Route to handle logout
@logout_bp.route('/logout', endpoint='logout', methods=['GET'])
def logout():
    # Clear the user session
    session.clear()
    # Redirect the user to the login page
    return redirect(url_for('login.login'))

