#!/usr/bin/env python3
""" Basic auth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic auth class """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header for a Basic Authentication """
        if len(str(authorization_header).split(" ")) == 2:
            if authorization_header \
                    is not None and 'Basic' \
                    in str(authorization_header).split(" ")[0]:
                return authorization_header.split(" ")[1]

        return None
