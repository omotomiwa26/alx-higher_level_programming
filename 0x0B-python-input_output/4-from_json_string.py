#!/usr/bin/python3
"""
This module returns an object
(Python data structure)
represented by a JSON string
"""
import json as j


def from_json_string(my_str):
    """
    Args:
        my_str: The JSON string to be converted.

    Returns:
        A Python data structure (object)
        represented by the JSON string.
    """
    obj = j.loads(my_str)
    return obj
