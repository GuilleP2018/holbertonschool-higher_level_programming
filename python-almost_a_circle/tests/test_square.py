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
        with self.assertRaises(TypeError):
            s = Square(4)
            s.size = "hello"

    def test_square_str(self):
        """str test"""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_update(self):
        """update test"""
        s = Square(4, 2, 1, 12)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 4")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 2")
        s.update(89, 2, 3)


if __name__ == '__main__':
    unittest.main()
