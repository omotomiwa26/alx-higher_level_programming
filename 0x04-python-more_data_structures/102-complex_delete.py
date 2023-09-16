#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []

    for key, element in a_dictionary.items():
        if element == value:
            delete_keys.append(key)

    for key in delete_keys:
        del a_dictionary[key]

    return a_dictionary