#!/usr/bin/python3
"""unittest for Base class"""


import unittest
from models.base import Base


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

    def test_b_to_json_string(self):
        """test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'x': 2}]), '[{"x": 2}]')
        self.assertEqual(Base.to_json_string([{'x': 2}, {'y': 1}]),
                         '[{"x": 2}, {"y": 1}]')

    def test_c_from_json_string(self):
        """test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"x": 2}]'), [{'x': 2}])
        self.assertEqual(Base.from_json_string('[{"x": 2}, {"y": 1}]'),
                         [{'x': 2}, {'y': 1}])

    def test_d_create(self):
        """test create method"""
        r1 = Base.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r2 = Base.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 1)
        r3 = Base.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.id, 89)

    def test_e_load_from_file(self):
        """test load_from_file method"""
        r1 = Base(98)
        r2 = Base(99)
        list_rectangles_input = [r1, r2]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                         list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                         list_rectangles_output[1].id)
        self.assertNotEqual(list_rectangles_input[0],
                            list_rectangles_output[0])
        self.assertNotEqual(list_rectangles_input[1],
                            list_rectangles_output[1])

    def test_f_save_to_file(self):
        """test save_to_file method"""
        r1 = Base(98)
        r2 = Base(99)
        list_rectangles_input = [r1, r2]
        Base.save_to_file(list_rectangles_input)
        list_rectangles_output = Base.load_from_file()
        self.assertEqual(list_rectangles_input[0].id,
                         list_rectangles_output[0].id)
        self.assertEqual(list_rectangles_input[1].id,
                         list_rectangles_output[1].id)
        self.assertNotEqual(list_rectangles_input[0],
                            list_rectangles_output[0])
        self.assertNotEqual(list_rectangles_input[1],
                            list_rectangles_output[1])


if __name__ == '__main__':
    unittest.main()
