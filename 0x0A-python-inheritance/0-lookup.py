#!/usr/bin/python3
"""
This module returns the lists of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Defining and initializing the
    attributes and objects
    """
    all_attributes = dir(obj)
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]
    attributes = [attr for attr in all_attributes if not
                  callable(getattr(obj, attr))]

    return {
        "attributes": attributes,
        "methods": methods
    }
