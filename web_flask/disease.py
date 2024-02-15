#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, send_from_directory
from models import storage
from models.disease import Disease 
import re
from sqlalchemy import func


# Define the blueprint
disease_bp = Blueprint('disease', __name__)


# Route to handle disease request5
@disease_bp.route('/disease', endpoint='disease', methods=['POST', 'GET'])
def disease():

    #the get method first
    if request.method == 'GET':
        return send_from_directory('servee_app', 'disease.html')
