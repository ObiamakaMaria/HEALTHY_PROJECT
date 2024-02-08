#!/usr/bin/env python3

# __init__.py

from flask import Flask
from web_flask.main_app import main_bp 

def create_app():
    app = Flask(__name__)
    # Register blueprints
    app.register_blueprint(main_bp)

    return app

