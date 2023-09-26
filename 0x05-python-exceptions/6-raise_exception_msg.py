#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except KeyboardInterrupt as e:
        print("keyboardInterupt Handled")
