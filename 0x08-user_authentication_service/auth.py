#!/usr/bin/env python3
""" auth class """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Transform to Hash format """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a new user with authentication """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            pwd_encrypt = _hash_password(password=password)
            return self._db.add_user(email=email, hashed_password=pwd_encrypt)
        else:
            raise ValueError("User {} already exists".format(email))
