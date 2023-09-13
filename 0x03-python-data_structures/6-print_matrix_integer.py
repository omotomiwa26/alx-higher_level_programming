#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        matrix_row = ""

        for index, int in enumerate(row):
            matrix_row += ("{:d} ".format(int))

            if index < len(row) - 1:
                matrix_row += " "

        print(matrix_row)
