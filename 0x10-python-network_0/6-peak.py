#!/usr/bin/python3
""" A  function that finds a peak in a list of unsorted integers.. """

def find_peak(list_of_integers):
    """
    rgs:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2
    mid_value = list_of_integers[mid]

    if (mid == 0 or mid_value >= list_of_integers[mid - 1]) and \
            (mid == len(list_of_integers) - 1 or
                    mid_value >= list_of_integers[mid + 1]):
                return mid_value

    if mid > 0 and mid_value < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    return find_peak(list_of_integers[mid + 1:])


