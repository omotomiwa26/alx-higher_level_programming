#!/usr/bin/python3
"""
    This module adds two integer numbers
    and returns the integer result
"""


def add_integer(a, b=98):
    """
       Define the integer values
       int a and int b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
