#!/usr/bin/python3
if __name__ == "__main__":

    """Output sum of all arguments."""
    import sys

    total = 0
    args = [int(arg) for arg in sys.argv[1:]]
    total = sum(args)

    print(total)
