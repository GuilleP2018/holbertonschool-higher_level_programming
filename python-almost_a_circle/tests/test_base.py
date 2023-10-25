#!/usr/bin/python3
"""unittest for Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """testing functions for Base class"""

    def test_a_base_instantiation(self):
        """test initialization of id if id None and if id int"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(73)
        self.assertEqual(b3.id, 73)
        b4 = Base()
        self.assertEqual(b4.id, 3)


class TestRectangleSquare(unittest.TestCase):
    def test_rectangle_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_square_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 1, 2, 42)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 42, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(r_dict, expected_dict)

    def test_create_from_dictionary(self):
        r_dict = {'id': 42, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        r = Rectangle.create(r_dict)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_square_size_property(self):
        s = Square(4)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_square_size_setter_validation(self):
        with self.assertRaises(ValueError):
            s = Square(4)
            s.size = -3


if __name__ == '__main__':
    unittest.main()
