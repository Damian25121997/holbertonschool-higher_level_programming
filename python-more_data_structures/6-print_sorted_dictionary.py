#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for kyes in sorted(a_dictionary.keys()):
        print("{}: {}".format(kyes, a_dictionary[kyes]))
