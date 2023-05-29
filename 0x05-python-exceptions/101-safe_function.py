#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ A funct that executes a function safely."""
    try:
        output = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    else:
        return output
