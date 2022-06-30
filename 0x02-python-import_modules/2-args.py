#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) < 2:
        print("1 argument.")
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
        print("{:d}: {:s}".format((len(argv) - 1), argv[1]))
    else:
        print("{} arguments".format(len(argv) - 1))
        while (i < len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
