#!/usr/bin/python3
def no_c(my_string):
    new_my_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_my_string += char

    return new_my_string
