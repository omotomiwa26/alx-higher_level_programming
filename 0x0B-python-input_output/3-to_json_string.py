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
    return j.dumps(my_obj)
