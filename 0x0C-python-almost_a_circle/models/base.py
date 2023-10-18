#!/usr/bin/python3
"""
This is the base module
for the project
"""

import json as j


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list
        of dictionaries.
        Args:
        - list_dictionaries: A list of dictionaries to be
        converted to a JSON string.
        Returns:
        - A JSON string representation of the list of
        dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return j.dumps(list_dictionaries)
