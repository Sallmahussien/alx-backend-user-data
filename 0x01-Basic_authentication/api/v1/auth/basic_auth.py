#!/usr/bin/env python3
"""Defines basic_auth module"""

from .auth import Auth


class BasicAuth(Auth):
    """Implement BasicAuth class"""
    def __init__(self) -> None:
        super().__init__()
