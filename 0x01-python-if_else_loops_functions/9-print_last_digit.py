#!/usr/bin/python3


def print_last_digit(number):
    if (number < 0):
        number *= -1
        digit = number % 10
    else:
        digit = number % 10
    print(f"{digit:d}", end='')
    return (digit)
