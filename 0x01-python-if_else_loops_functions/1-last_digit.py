#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = -(-number % 10)
else:
    last_number = (number) % 10

if last_number > 5:
    print(F"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
    print(F"Last digit of {number} is {last_number} and is 0")
else:
    print(F"Last digit of {number} is {last_number} and is less than 6 and not 0")
