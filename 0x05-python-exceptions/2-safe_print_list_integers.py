#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
        except (TypeError, ValueError):
            pass
        else:
            count += 1
    print()
    return count
