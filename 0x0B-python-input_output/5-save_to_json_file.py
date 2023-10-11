#!/usr/bin/python3
"""
This module writes an Object
to a text file, using a
JSON representation
"""
import json as j


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to JSON and save it to a text file.

    Args:
        my_obj: The object to be saved to the file.
        filename: The name of the file where the JSON
        representation will be stored.
    """
    with open(filename, "w") as file:
        j.dump(my_obj, file)
