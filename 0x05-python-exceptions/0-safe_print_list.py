#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for int in my_list:
            if count < x: 
                print(int, end="")
                count += 1
            else:
                 break
        print()
    except (NameError, RuntimeError, TypeError):
        pass
    return count
