#!/usr/bin/python3
"""Define the add ineger funcyion
"""


def add_integer(a, b=98):
    """"Function that adds two string.
    Args:
        a (int): First addend.
        b (int): Second addend.
    Return:
        int: The return value of result of add.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
