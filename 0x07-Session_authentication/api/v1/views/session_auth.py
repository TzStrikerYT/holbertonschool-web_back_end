#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_login():
    """ Auth Login
    """
    from api.v1.app import auth

    email = request.form.get('email', None)
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    pwd = request.form.get('password')
    if pwd is None or len(pwd) == 0:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(pwd):
            response = make_response(user.to_json())
            SESSION_NAME = os.getenv('SESSION_NAME')
            response.set_cookie(SESSION_NAME, auth.create_session(user.id))
            return response

    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout_session():
    """ Logout Session
    """
    from api.v1.app import auth

    if auth.destroy_session(request) is False:
        abort(401)

    return jsonify({}), 200
