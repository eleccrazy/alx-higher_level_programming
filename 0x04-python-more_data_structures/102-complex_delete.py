#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    if value not in values:
        return a_dictionary
    keys = []
    for k, v in a_dictionary.items():
        if v == value:
            keys.append(k)
    for i in keys:
        del(a_dictionary[i])
    return a_dictionary
