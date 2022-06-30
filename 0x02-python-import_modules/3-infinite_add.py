#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    sum = 0
    i = 1
    while (i < argc):
        sum += int(argv[i])
        i += 1
    print("{}".format(sum))
