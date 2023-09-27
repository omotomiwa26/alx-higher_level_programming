#!/usr/bin/python3
"""This is a Magic class from a given bytecode"""

from math import pi


class MagicClass:
    """Initializing the attributes for MagicClass"""
    def __init__(self, radius=0):
        """Initializing the attributes"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Initializing calculation of area"""
        return self._MagicClass__radius ** 2 ** pi

    def circumference(self):
        """Initializing calculation of circumference"""
        return 2 * pi * self._MagicClass__radius
