#!/usr/bin/python3
def raise_exception():
    try:
        raise BufferError("Ooops!, Cannot Read Buffer")
    except BufferError as e:
        print("Buffer Error Handled")
