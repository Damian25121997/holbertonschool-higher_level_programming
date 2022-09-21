#!/usr/bin/python3
"""Define the dividdes all elements of a matrix"""


def matrix_divided(matrix, div):
    """"Function divides all elements of a matrix.
    Args:
        matrix: is a matrix.
        div: number to divide the matrix.
    Return:
        The return new matrix.
    """
    if type(div) != int and type(div) != float:
        TypeError("div must be a number")
    if div == 0:
        TypeError("division by zero")
    new_matrix = []
    for element in matrix:
        new_list = []
        for i in element:
            if type(i) != int and type(i) != float:
                TypeError("matrix must be a matrix (list of lists) of integers/floats")
            x = i / div
            new_list.append(round(x, 2))
        new_matrix.append(new_list)
    return new_matrix
