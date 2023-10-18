#!/usr/bin/python3
"""
Unittest for square model
"""

import unittest as u
from models.square import Square
from models.base import Base



class TestSquare(u.TestCase):
    def test_square_with_int_attributes(self):
        square_instance = Square(4, 5, 6, 7)
        self.assertEqual(square_instance.size, 4)
        self.assertEqual(square_instance.x, 5)
        self.assertEqual(square_instance.y, 6)
        self.assertEqual(square_instance.id, 7)

    def test_square_with_default_int_attributes(self):
        square_instance = Square(9)
        self.assertEqual(square_instance.size, 9)
        self.assertEqual(square_instance.x, 0)
        self.assertEqual(square_instance.y, 0)
        self.assertIsNotNone(square_instance.id)


class TestSize(u.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            square_instance = Square(4.3)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            square_instance = Square('layi')

    def test_with_None(self):
        with self.assertRaises(TypeError):
            square_instance = Square(None)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            square_instance = Square(-2)


class TestX(u.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            square_instance = Square(4, 6.1)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            square_instance = Square(1, 'layi')

    def test_with_None(self):
        with self.assertRaises(TypeError):
            square_instance = Square(2, None)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            square_instance = Square(2, -6)


class TestY(u.TestCase):
    def test_with_float(self):
        with self.assertRaises(TypeError):
            square_instance = Square(2, 4.3)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            square_instance = Square(9, 'wasabi')

    def test_with_None(self):
        with self.assertRaises(TypeError):
            square_instance = Square(2, None)

    def test_with_negative(self):
        with self.assertRaises(ValueError):
            square_instance = Square(2, -7)


class TestArea(u.TestCase):
    def test_with_all_attributes(self):
        square_instance = Square(8, 0, 0)
        self.assertEqual(square_instance.area(), 64)

    def test_with_one_attributes(self):
        square_instance = Square(10)
        self.assertEqual(square_instance.area(), 100)


class TestFormatString(u.TestCase):
    def test_with_string_attr(self):
        square_instance = Square(3, 1, 3)
        self.assertEqual(str(square_instance), "[Square] 9 1/3 - 3")


class TestArgument(u.TestCase):
    def test_with_invalid_args(self):
        with self.assertRaises(TypeError):
            square_instance = Square(1, 2, 8, 4, 10, 8)


class TestUpadateArgs(u.TestCase):
    def test_update_with_args_attr(self):
        square = Square(2, 3, 4, 5)
        square.update(5, 4, 3, 2)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)

    def test_update_with_empty_args_attr(self):
        square = Square(1, 2, 3, 4)
        square.update()
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)


class TestUpadateKwargs(u.TestCase):
    def test_update_with_kwargs_attr(self):
        square = Square(4)
        square.update(id=1, x=2, y=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_with_empty_kwargs_attr(self):
        square = Square(5, 4)
        square.update()
        self.assertEqual(square.id, 16)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 0)


class TestSquareDict(u.TestCase):
    def test_with_all_dict_keys(self):
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        square_dict = {'id': 1, 'x': 2, 'y': 3, 'size': 5}
        self.assertEqual(dictionary, square_dict)

    def test_with_two_dict_keys(self):
        square = Square(5, 2)
        dictionary = square.to_dictionary()
        square_dict = {'id': 15, 'x': 2, 'y': 0, 'size': 5}
        self.assertEqual(dictionary, square_dict)


if __name__ == '__main__':
    u.main()