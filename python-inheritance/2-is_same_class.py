#!/usr/bin/python3
"""Write a function that returns True if the object is exactly an instance
of the specified class, otherwise False."""


def is_same_class(obj, a_class):
    """Funtion return True if the object is exactly an instance
    of the specified class, otherwise False

    Return: True or False
    """
    return True if type(obj) == a_class else False
