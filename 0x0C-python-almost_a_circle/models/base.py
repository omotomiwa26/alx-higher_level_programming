#!/usr/bin/python3
"""
This is the base module
for the project
"""


class Base:
    """
    Defining the base class with
    private attributes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Define constructor with
        instance attribute
        """

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
