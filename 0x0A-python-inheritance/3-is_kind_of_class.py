#!/usr/bin/python3
"""
This module returns True
if the object is an instance of, or if the object
is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Define and initialise the class object
    and inherited class
    """

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
