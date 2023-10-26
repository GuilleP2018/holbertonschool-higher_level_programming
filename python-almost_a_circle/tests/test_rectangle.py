#!/usr/bin/python3
"""unittest for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class tests"""

    def test_rectangle_area(self):
        """Area test"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_to_dictionary(self):
        """dictionary test"""
        r = Rectangle(4, 5, 1, 2, 42)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 42, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(r_dict, expected_dict)

    def test_rectangle_display(self):
        """display test"""
        r = Rectangle(2, 2)
        self.assertEqual(r.display(), None)

    def test_rectangle_str(self):
        """str test"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update(self):
        """update test"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 2/1 - 4/6")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 2/1 - 2/6")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 2/1 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/1 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == '__main__':
    unittest.main()
