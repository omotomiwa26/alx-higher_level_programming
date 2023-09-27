#!/usr/bin/python3
"""A class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class Square with Private instance attribute: size
    and Instantiation with optional size"""

    def __init__(self, size=0):
        """Initilizing the attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
