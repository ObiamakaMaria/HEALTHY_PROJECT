#!/usr/bin/env python3

# __init__.py

from flask import Flask
from web_flask.main_app import main_bp 
from web_flask.login import login_bp

def create_app():
    app = Flask(__name__)
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)

    return app

