#!/usr/bin/env python3
"""Defines basic_auth module"""

from .auth import Auth


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
