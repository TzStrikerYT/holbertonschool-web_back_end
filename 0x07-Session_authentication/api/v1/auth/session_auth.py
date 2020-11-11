#!/usr/bin/env python3
""" Session Auth module
"""
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import uuid
import os


class SessionAuth(Auth):
    """ Session Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session
        """
        if user_id is None or not isinstance(user_id, str):
            return

        session = str(uuid.uuid4())
        self.user_id_by_session_id[session] = user_id

        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return the session id
        """
        if session_id is None or not isinstance(session_id, str):
            return

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Current User
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Close the session
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if self.user_id_by_session_id.get(session_id, None) is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
