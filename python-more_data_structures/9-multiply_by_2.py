#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for x in new_dictionary.keys():
        new_dictionary[x] = new_dictionary[x] * 2
    return new_dictionary
