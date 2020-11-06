#!/usr/bin/env python3
""" API authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class that manages api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authentication check """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        slash = True if path[-1] == '/' else False
        path = path if slash is True else path + '/'

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ header check """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
