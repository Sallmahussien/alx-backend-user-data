#!/usr/bin/env python3
"""Defines basic_auth module"""

from .auth import Auth
import base64


class BasicAuth(Auth):
    """Implement BasicAuth class"""
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base64 from the header"""
        if (authorization_header is None
                or type(authorization_header) is not str
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Decode base64 header"""
        if (base64_authorization_header is None
                or type(base64_authorization_header) is not str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None
