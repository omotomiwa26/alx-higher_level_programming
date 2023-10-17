#!/usr/bin/python3
"""
This module defines the class Square
that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining and initialisng the Square class
    with the private instance attributes.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Define and inherits
        all poperties from Rectangle class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (F'[Square] {self.id} {self.x}/{self.y} - {self.width}')
