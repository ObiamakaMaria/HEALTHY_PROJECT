#!/usr/bin/env python3

""" This is the route that serve home page and index page """
# main_app.py

from flask import Blueprint, redirect, send_from_directory, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Serve the landing page
    return send_from_directory('servee_app', 'landing.html')
@main_bp.route('/home')
def home():
    # Redirect to the home page
    if "user_id" in session:
        return send_from_directory('servee_app', 'dashboard.html') 
    return send_from_directory('servee_app', 'home.html')
