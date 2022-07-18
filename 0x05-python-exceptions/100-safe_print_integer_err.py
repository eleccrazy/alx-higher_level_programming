#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    status = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        status = False
        msg = sys.exc_info()
        print("Exception: {}".format(msg[1]), file=sys.stderr)
    finally:
        return status
