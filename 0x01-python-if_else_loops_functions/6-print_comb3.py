#!/usr/bin/python3
for first_number in range(10):
    for second_number in range(first_number, 10):
        if second_number != first_number and (first_number != 8 or second_number != 9):
            print("{}{},".format(first_number, second_number), end=' ')
        elif first_number == 8 and second_number == 9:
            print("{}{}".format(first_number, second_number))
