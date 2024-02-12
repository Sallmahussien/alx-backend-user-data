#!/usr/bin/env python3
"""Authentications module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Implement Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = path + '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authrization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
