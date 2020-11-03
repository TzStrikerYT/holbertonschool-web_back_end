#!/usr/bin/env python3
""" Encrypt password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ hash encryption """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
