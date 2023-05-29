#!/usr/bin/python3
def safe_print_division(a, b):
    """ Function returning result of division of a & b."""
    try:
        result = int(a) / int(b)
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
