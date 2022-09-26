#!/usr/bin/python3
"""Function to return the list of avaliable attributes
and methods of an object"""


def lookup(obj):
    new_list = dir(obj)
    return list(new_list)
