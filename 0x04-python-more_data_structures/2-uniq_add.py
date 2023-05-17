#!/usr/bin/python3
def uniq_add(my_list=[]):
    result_list = []
    result = 0
    for item in my_list:
        if item not in result_list:
            result_list.append(item)
    for occurence in result_list:
        result += occurence
    return result
