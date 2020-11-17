#!/usr/bin/env python3
""" auth class """
import bcrypt


def _hash_password(password: str) -> str:
    """ Transform to Hash format """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
