#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        ln2 = len(i)
        for j in range(0, ln2):
            if j != ln2 - 1:
                print("{}".format(i[j]), end="")
            elif j == ln2 - 1:
                print("{}".format(i[j]))
