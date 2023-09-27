#!/usr/bin/python3
"""A class Square for getter and setter"""


class Square:
    """Private instance attribute: size
       property def size(self)
       property setter def size(self, value)
       Instantiation with optional size
       Public instance method: def area(self)"""

    def __init__(self, size=0):
        """Initilizing the attributes"""
        self.__size = size

    @property
    def size(self):
        """Getting the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Initializing attribute that returns the current square area"""
        return self.__size ** 2
