#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []

    for int in range(len(my_list)):
        if int != idx:
            new_list.append(my_list[int])

    return new_list
