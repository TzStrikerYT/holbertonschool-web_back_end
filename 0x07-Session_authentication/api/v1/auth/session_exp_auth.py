#!/usr/bin/env python3
""" Session expiration """
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import timedelta, datetime


class SessionExpAuth(SessionAuth):
    """ class for add date of expiration """

    def __init__(self):
        """ method constructor """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ return session id that created """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ return user id acording to the time """
        if session_id is None:
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if session_dictionary is None:
            return None

        user_id = session_dictionary.get('user_id')

        if user_id is None:
            return None

        if self.session_duration <= 0:
            return user_id

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        if datetime.now() > created_at + timedelta(
                seconds=self.session_duration
        ):
            return None

        return user_id
