#!/usr/bin/env python3

""" 
This is the module that runt the flask app
"""

from web_flask import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)
