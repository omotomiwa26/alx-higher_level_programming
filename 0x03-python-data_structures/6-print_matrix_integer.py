#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        matrix_row = ""

        for int in row:
            print("{:d}".format(int), end=" " if int != row[-1] else "")
        print()
