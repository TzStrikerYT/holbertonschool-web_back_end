#!/usr/bin/env python3
""" API authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Class that manages api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authentication check """
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ header check """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
