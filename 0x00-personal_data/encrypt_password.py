#!/usr/bin/env python3
"""Defines encrypt_password module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password,"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
