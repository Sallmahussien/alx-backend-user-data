#!/usr/bin/env python3
"""Defines auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a salted, hashed password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
