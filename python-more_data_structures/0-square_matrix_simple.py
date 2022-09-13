#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elements in matrix:
        new_list = []
        for i in elements:
            x = i * i
            new_list.append(x)
        new_matrix.append(new_list)
    return new_matrix
