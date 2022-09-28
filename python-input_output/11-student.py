#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for elem in attrs:
                if elem in self.__dict__.keys():
                    dic[elem] = self.__dict__[elem]
            return dic

    def reload_from_json(self, json):
        for items in json.keys():
            self.__dict__[items] = json[items]
