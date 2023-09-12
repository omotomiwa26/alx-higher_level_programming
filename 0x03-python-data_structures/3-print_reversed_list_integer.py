#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print("None")
    elif len(my_list) == 0:
        print("None")
    else:
        for int in reversed(my_list):
            print("{:d}".format(int))
