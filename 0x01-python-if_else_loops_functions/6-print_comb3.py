#!/usr/bin/python3
for first_number in range(10):
    for second_number in range(first_number + 1, 10):
        print("{}{},".format(first_number, second_number), end=' ')
        if first_number == 8 and second_number == 9:
            print("{}{}".format(first_number, second_number))
