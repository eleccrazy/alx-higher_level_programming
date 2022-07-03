#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len < 2 and a_len == 0:
        tuple_a = 0, 0
    if a_len < 2 and a_len == 1:
        tuple_a = tuple_a[0], 0
    if b_len < 2 and b_len == 0:
        tuple_b = 0, 0
    if b_len < 2 and b_len == 1:
        tuple_b = tuple_b[0], 0
    result = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return result
