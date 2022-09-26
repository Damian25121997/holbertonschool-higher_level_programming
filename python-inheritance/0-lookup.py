#!/usr/bin/python3
"""Function to return the list of avaliable attributes
and methods of an object"""


def lookup(obj):
    """Return the list of acaliable attributes and methods
    of an object
    
    obj: is an object
    """
    new_list = dir(obj)
    return list(new_list)
