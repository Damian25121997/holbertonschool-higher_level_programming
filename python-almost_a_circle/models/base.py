#!/usr/bin/python3
"""Defina a class Base"""


import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) == list:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        dic = []
        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))
        with open(file, 'w') as t:
            t.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)
