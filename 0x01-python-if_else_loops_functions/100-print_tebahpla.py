#!/usr/bin/python3


for i in reversed(range(96, 123)):
    if (not (i >= 91 and i <= 96)):
        if (i % 2 != 0):
            i -= 32
        print("{}".format(chr(i)), end='')
