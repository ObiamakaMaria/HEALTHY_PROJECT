#!/usr/bin/env python3

# main_app.py

from flask import Blueprint, redirect, send_from_directory

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Redirect to the home.html file
    return send_from_directory('servee_app', 'home.html')
