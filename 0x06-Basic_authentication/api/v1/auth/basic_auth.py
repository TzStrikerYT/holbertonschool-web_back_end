#!/usr/bin/env python3
""" Basic auth class"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic auth class """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """ Authorization header for a Basic Authentication """
        if len(str(authorization_header).split(" ")) == 2:
            if authorization_header \
                    is not None and 'Basic' \
                    in str(authorization_header).split(" ")[0]:
                return authorization_header.split(" ")[1]

        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """ returns the decoded value of a Base64 str """
        try:
            utf_val = base64_authorization_header.encode('utf-8')
            decode = b64decode(utf_val).decode('utf-8')
            return decode
        except (AttributeError, ValueError) as a:
            return None
