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
        self.assertEqual(str(s), "[Square] (89) 2/3 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 4/3 - 2")

    def test_square_update_kwargs(self):
        """update kwargs test"""
        s = Square(4, 2, 1, 12)
        s.update(size=1)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 1")
        s.update(size=1, x=2)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 1")
        s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 2")
        s.update(x=1, size=2, y=3, id=89)
        self.assertEqual(str(s), "[Square] (89) 1/3 - 2")

    def test_square_update_args_kwargs(self):
        """update args kwargs test"""
        s = Square(4, 2, 1, 12)
        s.update(89, size=2)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 2")
        s.update(89, 2, size=3)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 2")
        s.update(89, 2, 3, size=4)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 2")
        s.update(89, 2, 3, 4, size=5)
        self.assertEqual(str(s), "[Square] (89) 4/3 - 2")
        s.update(89, 2, 3, 4, 5, size=6)
        self.assertEqual(str(s), "[Square] (89) 4/3 - 2")

    def test_square_to_dictionary(self):
        """dictionary test"""
        s = Square(4, 2, 1, 12)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 12, 'size': 4, 'x': 2, 'y': 1}
        self.assertDictEqual(s_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
