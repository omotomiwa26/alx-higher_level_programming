#!/usr/bin/python3
"""
    This module defines a function 
    that prints a saqaure with the character #
"""


def print_square(size):
    """
        Defining the size of the square
        to print with the # character
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for _ in range(size):
        print('#' * size)
 