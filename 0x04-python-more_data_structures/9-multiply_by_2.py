#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = {}
    for keys in a_dictionary:
        new_dic[keys] = a_dictionary[keys] * 2
    return new_dic
