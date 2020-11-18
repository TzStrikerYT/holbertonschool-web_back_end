#!/usr/bin/env python3
""" auth class """
from uuid import uuid4
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Transform to Hash format """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generates a uuid """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Return true or false if credentials are correct """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode(),
                                  hashed_password=user.hashed_password)

    def create_session(self, email: str) -> str:
        """ find the user with the email, generates a new uuid and
        store in the database the session_id """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id
