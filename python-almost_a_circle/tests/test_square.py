#!/usr/bin/python3
"""Square Tests Module"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square class tests"""

    def test_square_area(self):
        """area test"""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_square_size_property(self):
        """size property test"""
        s = Square(4)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_square_size_setter_validation(self):
        """setter validation test"""
        with self.assertRaises(ValueError):
            s = Square(4)
            s.size = -3
