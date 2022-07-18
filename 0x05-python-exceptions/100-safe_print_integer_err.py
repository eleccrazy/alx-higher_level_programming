#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    status = True
    msg = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        status = False
        sys.stderr.write(msg)
    finally:
        return status
