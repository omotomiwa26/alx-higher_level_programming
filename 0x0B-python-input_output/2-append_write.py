#!/usr/bin/python3
"""
This module appends a string
at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Define and initialise the file that
    appends a text and creates the file
    if it dosent exist
    """
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)
    return len(text)
