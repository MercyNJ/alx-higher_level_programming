#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides 2 lists element by element
    Args:
        my_list_1 (list): The 1st list.
        my_list_2 (list): The 2nd list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of len list_length with all the divisions
    """

    new_list = []

    for element in range(0, list_length):
        try:
            div_result = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            new_list.append(div_result)
    return (new_list)
