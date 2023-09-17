#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(first_num, 10):
        if second_num != first_num and (first_num != 8 or second_num != 9):
            print("{}{},".format(first_num, second_num), end=' ')
        elif first_num == 8 and second_num == 9:
            print("{}{}".format(first_num, second_num))
