#!/usr/bin/python3
"""
This module creates an Object from a “JSON file"
"""
import json as j


def load_from_json_file(filename):
    """
    Load an object from a JSON file
    and return it as a
    Python data structure.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        A Python data structure representing
        the object loaded from the JSON file.
    """
    with open(filename, "r") as file:
        loaded_obj = j.load(file)
    return loaded_obj
