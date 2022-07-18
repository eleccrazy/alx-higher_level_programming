#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            count += 1
    except IndexError:
        pass
    print("")
    return (count)
