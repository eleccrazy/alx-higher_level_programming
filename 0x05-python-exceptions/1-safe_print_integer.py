#!/usr/bin/python3


def safe_print_integer(value):
    status = True
    try:
        print("{:d}".format(value))
    except ValueError:
        status = False
    return status
