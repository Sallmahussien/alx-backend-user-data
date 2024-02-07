#!/usr/bin/env python3
"""Defines filtered_loger module"""

from typing import List
import re


def filter_datum(
        fields: List[int], redaction: str, message: str, separator: str
        ) -> str:
    """Returns the log message obfuscated."""
    for field in fields:
        pattern = rf"{field}=[a-zA-Z0-9\/]+{separator}"
        replacement = f"{field}={redaction}{separator}"
        message = re.sub(pattern, replacement, message)

    return message
