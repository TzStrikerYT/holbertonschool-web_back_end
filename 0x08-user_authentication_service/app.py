#!/usr/bin/env python3
""" APP """
from flask import jsonify, Flask, request, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def main():
    """ Main execute """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def get_user():
    """ Get an user """
    email = request.form.get('email')
    passwd = request.form.get('password')

    if email is None or passwd is None:
        abort(400)

    try:
        user = AUTH.register_user(email=email, password=passwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({
            "email": f"{user.email}",
            "message": "user created"
        }), 200


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """ Generates a response when the users logged in"""
    email = request.form.get('email')
    passwd = request.form.get('password')

    if email is None or passwd is None:
        abort(401)

    is_valid = AUTH.valid_login(email=email, password=passwd)

    if is_valid is False:
        abort(401)

    session = AUTH.create_session(email=email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie("session_id", session)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout the session
    """
    session = request.cookies.get('session_id')
    if session is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id=session)

    if user is None:
        abort(403)

    AUTH.destroy_session(user_id=user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
