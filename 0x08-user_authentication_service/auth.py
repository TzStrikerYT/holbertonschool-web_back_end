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

    def get_user_from_session_id(self, session_id: str) -> str:
        """ find user from session_id """

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        if user.session_id is None:
            return None
        else:
            return user

    def destroy_session(self, user_id: int) -> None:
        """Close the session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """ Generates an uuid for reset the passwd """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        user.reset_token = _generate_uuid()
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            user.hashed_password = _hash_password(password=password)
            user.reset_token = None
