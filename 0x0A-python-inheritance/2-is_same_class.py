#!/usr/bin/python3
"""
This module returns True, If the object
is exactly an instance of the specified class;
Else returns False
"""


def is_same_class(obj, a_class):
    """
    Define and initialize the objects
    in class
    """
    if isinstance(obj, a_class):
        if issubclass(type(obj), a_class):
            return False
        return True
    else:
        return False
