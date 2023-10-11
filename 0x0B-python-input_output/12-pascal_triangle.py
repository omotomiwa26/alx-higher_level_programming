#!/usr/bin/python3
"""
This module Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Args:
        attrs (n): This is the integer arguement
        passed to generate and print the number
        of rows of the Pascal's triangle.

    Returns: The list of lists on integers representing
             the Pascal's Triangle
    """

    if n <= 0:
        return []

    pascal_triangle = []

    for x in range(n):
        row = []
        for y in range(x + 1):
            if y == 0 or y == x:
                row.append(1)
            else:
                value = pascal_triangle[x - 1][y - 1]
                + pascal_triangle[x - 1][y]
                row.append(value)
        pascal_triangle.append(row)

    return pascal_triangle
