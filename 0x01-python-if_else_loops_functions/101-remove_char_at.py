#!/usr/bin/python3


def remove_char_at(str, n):
    temp = ""

    for c in str:
        if n != 0:
            temp += c
        n -= 1

    return temp
