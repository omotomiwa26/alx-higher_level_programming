#!/usr/bin/python3
"""
This module reads a text file (UTF8)
and prints it to stdout:
"""


def read_file(filename=""):
    """
    define and initialise the file to open
    in read only mode and encoding UTF8
    """

    with open(filename, "r", encoding="UTF8") as file:
        print(file.read(), end='')
