#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colmn in row:
            if colmn == row[-1]:
                print('{:d}'.format(colmn), end='')
            else:
                print('{:d}'.format(colmn), end=' ')
        print()
