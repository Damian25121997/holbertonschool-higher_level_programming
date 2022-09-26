#!/usr/bin/python3
"""Write a class MyList that inheritis from list"""


class MyList(list):

    def print_sorted(self):
        """Write a class MyList that inheritis from list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
