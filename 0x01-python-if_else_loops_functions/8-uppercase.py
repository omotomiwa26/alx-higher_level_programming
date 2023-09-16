#!/usr/bin/python3
def uppercase(str):
    char_str = ""

    for char in str:
        if  'a' <= char <= 'z':
            char_str += chr(ord(char) - 32)
        else:
            char_str += char
    print("{}".format(char_str))
