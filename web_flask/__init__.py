#!/usr/bin/env python3

# __init__.py

from flask import Flask, redirect, url_for, session, request
from web_flask.main_app import main_bp 
from web_flask.login import login_bp
from web_flask.register import register_bp
from web_flask.logout import logout_bp
from web_flask.article import article_bp
from web_flask.disease import disease_bp
from web_flask.subscribe import subscribe_bp
from web_flask.search import search_bp
import secrets




def create_app():
    app = Flask(__name__)
    
    secret_key = secrets.token_hex(32)

    # Set the secret key
    app.secret_key = secret_key
    app.config['DEBUG'] = True

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(article_bp)
    app.register_blueprint(disease_bp)
    app.register_blueprint(subscribe_bp)
    app.register_blueprint(search_bp)

    return app

