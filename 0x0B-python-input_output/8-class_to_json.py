#!/usr/bin/python3
"""
This module returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Define and initialize the dict objects
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError('Object is not an instance of a class')

    obj_dict = obj.__dict__
    return obj_dict
