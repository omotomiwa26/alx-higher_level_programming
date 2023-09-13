#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_2 import add, sub, mul, div
    from sys import argv, exit
    operator = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }

    if len(argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    operand = argv[2]
    b = int(argv[3])

    if operand not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operator[operand](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, operand, b, result))
