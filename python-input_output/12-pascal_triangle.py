#!/usr/bin/python3
"""Function return a list of lists of integers representing
the Pascal's triangle"""


def pascal_triangle(n):
    """Function return Pascal's triangle"""

    if n <= 0:
        return []

    list = []
    for elem in range(n):
        if elem == 0:
            list.append([1])
            continue
        if elem == 1:
            list.append([1, 1])
            continue
        aux = []
        for item in range(elem + 1):
            aux.append(item)
        for item in range(1, elem):
            aux[0] = 1
            aux[elem] = 1
            aux[item] = list[elem - 1][item] + list[elem - 1][item - 1]
        list.append(aux)
    return list
