#!/usr/bin/python3
"""
This module write a class Square
that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Define and initialise class square

    Args:
        Rectangle:
    """
    def __init__(self, size):
        """
        Args:
            size:
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        define and initialise area
        """
        return super().area()

    def __str__(self):
        """
        Define and initialise string to print
        and return sqaure discription
        """
        return F"[square] {self.__size}/{self.__size}"
