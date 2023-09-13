#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maximum_int = my_list[0]

    for int in my_list[1:]:

        if int > maximum_int:
            maximum_int = int

    return maximum_int
