#!/usr/bin/env python3
""" API authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class that manages api authentication"""

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
        """ header check """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
