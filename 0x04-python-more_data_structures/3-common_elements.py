#!/usr/bin/python3
def common_elements(set_1, set_2):
    in_both = set()

    for i in set_1:
        if i in set_2:
            in_both.add(i)
    return in_both
