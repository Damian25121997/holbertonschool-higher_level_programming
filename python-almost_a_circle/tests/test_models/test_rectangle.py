#!/usr/bin/python3
"""Test of rectangle class"""


from io import StringIO
from unittest import TestCase, mock
import json
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Test the funcionality of the rectangle class"""

    @classmethod
    def setUpClass(cls):
        """setting up class"""
        cls.r1 = Rectangle(10, 10, 0, 0, 5)
        cls.r2 = Rectangle(2, 3, 4, 0, 0)

    def test_width(self):
        """Testing for functioning width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)

    def test_height(self):
        """Testing for functioning height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

    def test_more(self):
        """Test for functioning more data in the class"""
        self.assertEqual(self.r1.id, 5)

    def test_width(self):
        """ width"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height(self):
        """height"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_width_typeerror(self):
        """Test not int for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)

    def test_height_typeerror(self):
        """not int for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")

    def test_x_typeerror(self):
        """not int for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")

    def test_y_typeerror(self):
        """not int for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")

    def test_width_valueerror(self):
        """ ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Test area"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (5) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (0) 4/0 - 2/3")

    def test_display(self):
        with mock.patch('sys.stdout', new=StringIO()) as output1:
            self.r2.display()
            self.assertEqual(output1.getvalue(), '    ##\n    ##\n    ##\n')

    def test_dispay2(self):
        with mock.patch('sys.stdout', new=StringIO()) as output2:
            self.r1.display()
            self.assertEqual(output2.getvalue(), '##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n##########\n')

    def test_to_dictionary(self):
        d1 = self.r1.to_dictionary()
        self.assertEqual({"id": 5, "width": 10, "height": 10, "x": 0, "y": 0}, d1)
        self.assertTrue(type(d1) is dict)