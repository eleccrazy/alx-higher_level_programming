#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret_val = fct(*args)
    except Exception:
        msg = sys.exc_info()
        print("Exception: {}".format(msg[1]), file=sys.stderr)
        ret_val = None
    finally:
        return ret_val
