#!/usr/bin/python3
"""
This module write a class Rectangle that
inherits from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Define and initialise the Rectangle class
    """

    def __init__(self, width, height):
        """
        initialise Instances

        Args:
            width:
            height:
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Define and initialise method to calculate
        and return the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Define method to print
        and return string
        """
        return F"[Rectangle] {self.__width:d}/{self.__height:d}"
