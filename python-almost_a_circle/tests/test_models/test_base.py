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
