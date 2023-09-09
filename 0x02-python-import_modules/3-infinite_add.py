#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) >= 3:
        total = 0
        for argv in sys.argv[1:]:
            total += int(argv)
        print(total)
    else:
        print("Command-Line Argument Addition Error")
