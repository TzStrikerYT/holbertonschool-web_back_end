#!/usr/bin/env python3
""" APP """
from flask import jsonify, Flask, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
