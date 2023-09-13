#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        matrix_row = ""

        for int in row:
            matrix_row += ("{:d} ".format(int))

        print(matrix_row)
