#!/usr/bin/python3
"""
    This module checks a given text and prints
    two new lines after each of the following
    characters ".", "?", ":"
"""


def text_indentation(text):
    """
        Defining the function for the given text
        and specified characters ".", "?", ":"
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = []
    current_text = ''
    for char in text:
        if char in '.?:':
            new_text.append(current_text.strip())
            current_text = ''
        else:
            current_text += char

    if current_text:
        new_text.append(current_text.strip())

    for text_string in new_text:
        print(text_string)
