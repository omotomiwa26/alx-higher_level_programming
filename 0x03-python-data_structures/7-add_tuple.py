#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    add_tuple = int(a[0]) + int(b[0]), int(a[1]) + int(b[1])

    return add_tuple
