#!/usr/bin/python3
"""
This module  inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (str): The name of the file to open and modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing
        the search string.
    """

    output_line = []
    with open(filename, "r", encoding="UTF8") as file:
        for line in file:
            output_line += [line]
            if line.find(search_string) != -1:
                output_line += [new_string]

    with open(filename, "w", encoding="UTF8") as file:
        file.write("".join(output_line))
