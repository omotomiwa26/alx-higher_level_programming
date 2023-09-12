#!/usr/bin/env python3
def no_c(my_string):
    new_my_string = []
    for char in my_string:
        if char.lower != 'c':
            new_my_string.append(char)

    return ''.join(new_my_string)
