#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))
