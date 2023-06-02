#!/usr/bin/python3
"""

Module contains function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        Nothing

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    temp = text[:]

    for punctuation in ".?:":
        list_text = temp.split(punctuation)
        temp = ""
        for i in list_text:
            i = i.strip(" ")
            temp = i + punctuation if temp is "" else temp + "\n\n" + i + punctuation

    print(temp[:-3], end="")
