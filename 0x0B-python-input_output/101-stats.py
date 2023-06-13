#!/usr/bin/python3
"""Reads from std input and calculates metrics.

After each 10 lines or keyboard interruption (CTRL + C),it
prints these stats:
    - Total file size to current reached point.
    - Count of read status codes to reached point.
"""


def print_stats(size, status_codes):
    """Print total metrics.

    Args:
        size (int): Total file size read.
        status_codes (dict): The accumulated total of status codes.
    """

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    accepted_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in accepted_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
