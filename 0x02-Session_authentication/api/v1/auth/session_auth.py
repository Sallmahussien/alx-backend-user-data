#!/usr/bin/env python3
"""Defines session_auth module"""

from .auth import Auth


class SessionAuth(Auth):
    """Implement SessionAuth class"""
    def __init__(self) -> None:
        super().__init__()
