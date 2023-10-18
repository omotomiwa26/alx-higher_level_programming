#!/usr/bin/python3
"""
This module defines the class Square
that inherits from Rectangle
"""

import json as j
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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return (F'[Square] {self.id} {self.x}/{self.y} - {self.width}')

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square using both
        *args and **kwargs.
        Arguments:
        - args: A tuple of arguments in the following order:
            1. id attribute
            2. size attribute
            3. x attribute
            4. y attribute
        - kwargs: A dictionary where each key
        represents an attribute to update.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == 'size':
                    self.width = value
                    self.height = value

    def to_dictionary(self):
        """
        Return a dictionary representation of the Sqaure.
        Returns:
        - A dictionary with the following keys:
            - 'id': The id attribute of the Square
            - 'size': The size attribute of the Square
            - 'x': The x attribute of the Square
            - 'y': The y attribute of the Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
