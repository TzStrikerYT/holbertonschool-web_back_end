#!/usr/bin/env python3
""" Use a Database to save the info
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import timedelta, datetime


class SessionDBAuth(SessionExpAuth):
    """ Session to use a DB
    """

    def create_session(self, user_id=None):
        """ Create Session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return

        user_session = UserSession(**{'user_id': user_id,
                                      'session_id': session_id})
        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Get the user id for session
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        session_ids = UserSession.search({'session_id': session_id})

        if len(session_id) == 0:
            return None

        if datetime.now() > session_ids[0].created_at + timedelta(
                seconds=self.session_duration
        ):
            return None

        return session_ids[0].user_id

    def destroy_session(self, request=None):
        """ Destroy the session
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        session_ids = UserSession.search({'session_id': session_id})
        if len(session_ids) == 0:
            return False

        try:
            session_ids[0].remove()
            session_ids[0].save()
            UserSession.save_to_file()
        except Exception:
            return False

        return True