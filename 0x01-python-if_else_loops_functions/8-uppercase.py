#!/usr/bin/python3


def uppercase(str):
    for ch in str:
        temp = ord(ch)
        if (temp > 96 and temp < 123):
            temp = ord(ch) - 32

        print("{:s}".format(chr(temp)), end='')
    print('')
