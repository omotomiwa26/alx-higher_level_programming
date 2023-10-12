#!/usr/bin/python3
"""
This module returns True if the object is an
instance of a class that inherited
(directly or indirectly) from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
     Define and initialise the attributes
     obj and a_class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
