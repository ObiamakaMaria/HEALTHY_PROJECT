#!/usr/bin/env python3

""" This module creates a route for searching on YouTube through API """

from flask import Blueprint, request, jsonify
from os import getenv
import requests

# Define the blueprint
search_bp = Blueprint('search', __name__)

# Route to handle the POST request for searching on YouTube
@search_bp.route('/search',  methods=['POST'])
def search():

    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    page_token = request.json.get('pageToken')
    results, next_page_token = fetch_results(query, page_token)

    return jsonify({'results': results, 'nextPageToken': next_page_token})

def fetch_results(query, page_token):
    api_key = getenv('DB_YTB_API')
    max_results_per_request = 5

    health_query = "{} health".format(query)
    url = ("https://www.googleapis.com/youtube/v3/search?key={}&"
           "part=snippet&type=video&q={}&maxResults={}&pageToken={}").format(api_key, health_query, max_results_per_request, page_token)
    
    try:
        response = requests.get(url)
        data = response.json()
        next_page_token = data.get('nextPageToken', '')
        items = data.get('items', [])

        filtered_results = filter_results(items)
        return filtered_results, next_page_token
    except Exception as e:
        return [], ''

def filter_results(items):
    filtered_results = []

    for item in items:
        if 'liveStreamingDetails' not in item.get('snippet', {}) and 'playlistId' not in item.get('snippet', {}):
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_url = "https://www.youtube.com/embed/{}".format(video_id)
            filtered_results.append({'videoId': video_id, 'title': video_title, 'url': video_url})

    return filtered_results

