#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        space = ""
        for j in k:
            print("{:s}{:d}".format(space, j), end="")
            space = " "
        print()
