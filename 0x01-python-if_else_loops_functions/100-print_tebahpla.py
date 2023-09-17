#!/usr/bin/python3
for char_alpha in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_alpha)
    print("{}".format(char if char_alpha % 2 == 0 else char.upper()), end='')
