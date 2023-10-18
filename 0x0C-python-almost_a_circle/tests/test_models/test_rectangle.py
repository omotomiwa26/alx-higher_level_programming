#!/usr/bin/python3
"""
Unittest for rectangle model
"""

import unittest as u
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(u.TestCase):
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


class TestWidth(u.TestCase):
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


class TestHeight(u.TestCase):
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


class TestX(u.TestCase):
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


class TestY(u.TestCase):
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


class TestArea(u.TestCase):
    def test_with_all_attributes(self):
        rectangle_instance = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(rectangle_instance.area(), 20)

    def test_with_width_and_height(self):
        rectangle_instance = Rectangle(7, 8)
        self.assertEqual(rectangle_instance.area(), 56)


class TestFormatString(u.TestCase):
    def test_with_string_attr(self):
        rectangle_instance = Rectangle(3, 2, 1, 1, 4)
        self.assertEqual(str(rectangle_instance), "[Rectangle] (4) 1/1 - 3/2")


class TestArgument(u.TestCase):
    def test_with_invalid_args(self):
        with self.assertRaises(TypeError):
            rectangle_instance = Rectangle(1, 2, 8, 4, 10, 8)


class TestUpadateArgs(u.TestCase):
    def test_update_with_args_attr(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(5, 4, 3, 2, 1)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)

    def test_update_with_empty_args_attr(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update()
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)


class TestUpadateKwargs(u.TestCase):
    def test_update_with_kwargs_attr(self):
        rectangle = Rectangle(5, 4)
        rectangle.update(id=1, x=2, y=3)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_update_with_empty_kwargs_attr(self):
        rectangle = Rectangle(5, 4)
        rectangle.update()
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)


class TestRecDict(u.TestCase):
    def test_with_all_dict_keys(self):
        rectangle = Rectangle(5, 2, 3, 1)
        dictionary = rectangle.to_dictionary()
        rectangle_dict = {'id': 2, 'x': 3, 'y': 1, 'height': 2, 'width': 5}
        self.assertEqual(dictionary, rectangle_dict)

    def test_with_two_dict_keys(self):
        rectangle = Rectangle(5, 2)
        dictionary = rectangle.to_dictionary()
        rectangle_dict = {'id': 3, 'x': 0, 'y': 0, 'height': 2, 'width': 5}
        self.assertEqual(dictionary, rectangle_dict)


if __name__ == '__main__':
    u.main()
