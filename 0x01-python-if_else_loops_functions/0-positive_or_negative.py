#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(F"{number} is positve\n")
elif number == 0:
    print(F"{number} is zero\n")
else:
    print(F"{number} is negative\n")
