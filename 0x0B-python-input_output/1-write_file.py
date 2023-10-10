#!/usr/bin/python3
"""
This writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Define and initialise the file in
    write mode, this should create the file
    if it does not exist and overite the text
    to write in the file
    """
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
    return len(text)
