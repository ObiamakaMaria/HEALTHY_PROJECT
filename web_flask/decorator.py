#!/usr/bin/env python3

""" This module is the decorator for protecting routes and pages """

from flask import session, request, redirect, url_for
from functools import wraps

def require_login(view_func):

    @wraps(view_func)
    def decorated_function(*args, **kwargs):
         if 'user_id' not in session and request.endpoint not in ['login', 'register']:
            return redirect(url_for('login.login'))
         return view_func(*args, **kwargs)
    return decorated_function

