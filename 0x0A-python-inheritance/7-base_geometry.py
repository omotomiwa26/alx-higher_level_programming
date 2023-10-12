#!/usr/bin/python3
"""
This module write a class BaseGeometry
(based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Empty Class
    """

    def area(self):
        """
        Define and initialise the public instance method

        Args:
            self:
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Define and initialise public instance method

        Args:
            name:
            value:
        """
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
