#!/usr/bin/env python3

""" This is the module that handles route related to articles """

from flask import Blueprint, request, jsonify, session, send_from_directory
from models import storage
from models.user import User
from models.article import Article
from web_flask.decorator import require_login

# Define the blueprint
article_bp = Blueprint('article', __name__)

# Route to handle the GET request to display the article form
@article_bp.route('/article',  methods=['GET'])
@require_login
def show_article_form():
    return send_from_directory('servee_app', 'article_form.html')

# Route to handle the POST request to save the article
@article_bp.route('/article',  methods=['POST'])
@require_login
def save_article():
    # Get the user ID from the session
    user_id = session.get('user_id')

    # Get the title and content of the article from the form data
    title = request.json.get('title')
    content = request.json.get('content')

    # Validate the input fields (add your validation logic here)
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400

    if len(title) > 50:
        return jsonify({'error': 'Title length cannot exceed 50 characters'}), 400

    if len(title) < 5:  # Example: Minimum title length of 5 characters
        return jsonify({'error': 'Title must be at least 5 characters long'}), 400

    # Create a new Article object and save it to the database
    article = Article(author_id=user_id, title=title, content=content)
    article.save()
    return jsonify({'message': 'Article saved successfully'}), 201   
