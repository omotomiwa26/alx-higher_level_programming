#!/usr/bin/python3
''''def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] =value

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        value = a_dictionary[key]
        print(F"{key}: {value}")'''

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)
