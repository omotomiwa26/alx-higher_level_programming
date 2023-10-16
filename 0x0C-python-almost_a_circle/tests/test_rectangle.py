#!/usr/bin/python3
"""
Unittest for rectangle model
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_with_int_attributes(self):
        rectangle_instance = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 6)
        self.assertEqual(rectangle_instance.y, 7)
        self.assertEqual(rectangle_instance.id, 8)

    def test_rectangle_with_default_int_attributes(self):
        rectangle_instance = Rectangle(1, 2)
        self.assertEqual(rectangle_instance.width, 1)
        self.assertEqual(rectangle_instance.height, 2)
        self.assertEqual(rectangle_instance.x, 0)
        self.assertEqual(rectangle_instance.y, 0)
        self.assertIsNotNone(rectangle_instance.id)


class TestWidth(unittest.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(4.3, 5, 6, 7, 8)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle('layi', 5, 6, 7, 8)

    def test_with_None(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(None, 5, 6, 7, 8)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(-2, 5, 6, 7, 8)


class TestHeight(unittest.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(4, 5.1, 6, 7, 8)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(2, 'wasabi', 6, 7, 8)

    def test_with_None(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(4, None, 6, 7, 8)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(6, -4, 6, 7, 8)


class TestX(unittest.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(4, 5, 6.1, 7, 8)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(1, 5, 'layi', 7, 8)

    def test_with_None(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(2, 5, None, 7, 8)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(2, 5, -6, 7, 8)


class TestY(unittest.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(2, 5, 6, 4.3, 8)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(9, 5, 6, 'wasabi', 8)

    def test_with_None(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(2, 5, 6, None, 8)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            rectangle_instance = Rectangle(2, 5, 6, -7, 8)


class TestArea(unittest.TestCase):
    def test_with_all_attributes(self):
        rectangle_instance = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(rectangle_instance.area(), 20)

    def test_with_width_and_height(self):
        rectangle_instance = Rectangle(7, 8)
        self.assertEqual(rectangle_instance.area(), 56)


class TestFormatString(unittest.TestCase):
    def test_with_string_attr(self):
        rectangle_instance = Rectangle(3, 2, 1, 1, 4)
        self.assertEqual(str(rectangle_instance), "[Rectangle] (4) 1/1 - 3/2")


if __name__ == '__main__':
    unittest.main()
