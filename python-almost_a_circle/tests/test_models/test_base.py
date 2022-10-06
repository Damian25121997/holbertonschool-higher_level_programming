#!/usr/bin/python3
"""Test of base class"""


import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Check functionality of Base Class"""

    def test_no_id(self):
        """Testing id as None"""
        b = Base()
        self.assertAlmostEqual(b.id, 1)

    def test_no_id_after(self):
        """Testing id as None after not None"""
        b = Base()
        self.assertAlmostEqual(b.id, 2)

    def test_id_set(self):
        """Testing id as not None"""
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_to_json_string(self):
        """Testing regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_None_to_json_String(self):
        """testting None to a json"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests normal from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})
