#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Private instance attribute: size
       Instantiation with optional size
       Public instance method: def area(self)"""

    def __init__(self, size=0):
        """Initilizing attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Initializing attribute that returns the current square area"""
        return self.__size ** 2
