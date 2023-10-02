#!/usr/bin/python3
"""
    This module function divides all elements
    of a matrix which must be a lists
    of integers or floats.
"""


def matrix_divided(matrix, div):
    """
        Define the matrix elements as an
        integer or float.
    """

    if not all(isinstance(row, list)
               and all(isinstance(elements, (int, float))
                       for elements in row) for row in matrix):
        raise TypeError(F"matrix must be a matrix (list of lists)"
                        F"of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elements / div, 2)
                   for elements in row] for row in matrix]

    return new_matrix
