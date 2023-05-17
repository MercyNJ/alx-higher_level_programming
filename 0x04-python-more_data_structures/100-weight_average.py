#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_total = 0
    weight_total = 0

    for score, weight in my_list:
        sum_total += score * weight
        weight_total += weight

    if weight_total == 0:
        return 0

    return sum_total / weight_total
