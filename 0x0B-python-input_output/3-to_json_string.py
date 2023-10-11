#!/usr/bin/python3
"""
This module returns the JSON
representation of an object (string)
"""
import json as j


def to_json_string(my_obj):
    """
    Define and initialise the JSON
    object
    """
    json_strings = j.dumps(my_obj)
    return json_strings
