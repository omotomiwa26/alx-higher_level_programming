#!/usr/bin/python3
"""This class defines a square by: (based on 5-square.py)"""


class Square:
    """Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self)."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the attributes."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getting the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting size value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """sets value position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Initializing attribute tah returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Initialzing attributes that the square with the character
           #, to standard output at the position given
           by the position attribute"""

        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for y in range(0, self.__size):
            for a in range(0, self.__position[0]):
                print(" ", end="")
            for b in range(0, self.__size):
                print("#", end="")
            print()
