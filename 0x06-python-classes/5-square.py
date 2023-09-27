#!/usr/bin/python3
"""This class defines a square by: (based on 4-square.py)"""


class Square:
    """.Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self)"""

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

    def are(self):
        """Initializing attributes that returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Initializing attributes that prints to standard output
           the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()
