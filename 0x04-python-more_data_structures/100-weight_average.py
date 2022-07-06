#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s = 0
    di = 0
    for i in range(len(my_list)):
        s += (my_list[i][0] * my_list[i][1])
        di += my_list[i][1]
    return s / di
