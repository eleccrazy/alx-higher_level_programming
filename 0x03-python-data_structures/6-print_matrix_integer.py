#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        count = 0
        for col in rows:
            count += 1
            print("{:d}".format(col), end="" if not count < len(rows) else " ")
        print()
