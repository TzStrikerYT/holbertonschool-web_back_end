#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if len(path) == 0:
            return True

        slash = True if path[len(path) - 1] == '/' else False

        tmp_path = path if slash else path + '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Return None
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None

    def session_cookie(self, request=None):
        """ Get the cookie
        """
        if request is None:
            return

        if os.getenv('SESSION_NAME') is None:
            return

        return request.cookies.get(os.getenv('SESSION_NAME'))
