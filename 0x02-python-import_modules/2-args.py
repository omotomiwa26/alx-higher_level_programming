#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        argv1 = sys.argv[1]
        print("1:", argv1)
    elif len(sys.argv) == 3:
        print("2 arguments:")
        argv1 = sys.argv[1]
        argv2 = sys.argv[2]
        print("1:", argv1)
        print("2:", argv2)
    elif len(sys.argv) == 4:
        print("3 arguments:")
        argv1 = sys.argv[1]
        argv2 = sys.argv[2]
        argv3 = sys.argv[3]
        print("1:", argv1)
        print("2:", argv2)
        print("3:", argv3)
    elif len(sys.argv) == 5:
        print("4 arguments:")
        argv1 = sys.argv[1]
        argv2 = sys.argv[2]
        argv3 = sys.argv[3]
        argv4 = sys.argv[4]
        print("1:", argv1)
        print("2:", argv2)
        print("3:", argv3)
        print("4:", argv4)
    else:
        print("Ooops! More Than Four Arguments")
