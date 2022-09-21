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
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    new_matrix = []
    for element in matrix:
        if type(element) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                 integers/floats")
        new_list = []
        for i in element:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
            x = i / div
            new_list.append(round(x, 2))
        new_matrix.append(new_list)
    len_list = len(matrix[0])
    for r in matrix:
        if len(r) != len_list:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
