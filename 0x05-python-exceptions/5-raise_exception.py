#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Ooops!, Invalid Type")
    except BufferError as e:
        print("BufferError Handled")
