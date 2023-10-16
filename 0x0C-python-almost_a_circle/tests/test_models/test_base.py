#!/usr/bin/bash
"""
Unittest for base models
"""
import unittest as u
from models.base import Base


class TestBase(u.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_with_id(self):
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(25)
        self.assertEqual(base_instance.id, 25)
        base_instance = Base(102)
        self.assertEqual(base_instance.id, 102)
        base_instance = Base(0)
        self.assertEqual(base_instance.id, 0)

    def test_case_without_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base()
        self.assertEqual(base_instance.id, 2)

    def test_base_increment_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base()
        self.assertEqual(base_instance.id, 2)
        base_instance = Base()
        self.assertEqual(base_instance.id, 3)
        base_instance = Base()
        self.assertEqual(base_instance.id, 4)

    def test_base_with_negative_id_increment_id(self):
        base_instance = Base(-1)
        self.assertEqual(base_instance.id, -1)
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base()
        self.assertEqual(base_instance.id, 2)
        base_instance = Base()
        self.assertEqual(base_instance.id, 3)

    def test_base_with_negative_id(self):
        base_instance = Base(-1)
        self.assertEqual(base_instance.id, -1)
        base_instance = Base(-25)
        self.assertEqual(base_instance.id, -25)
        base_instance = Base(-102)
        self.assertEqual(base_instance.id, -102)

    def test_base_with_two_args(self):
        with self.assertRaises(TypeError):
            Base(4, 6)

    def test_base_with_string_id(self):
        base_instance = Base("layi")
        self.assertEqual(base_instance.id, "layi")
        base_instance = Base("wasabi")
        self.assertEqual(base_instance.id, "wasabi")

    def test_base_documented_module(self):
        # Tests for the module docstring
        self.assertTrue(len(__doc__) >= 2)

    def test_documented_class(self):
        # Tests for the Base class docstring
        self.assertTrue(len(Base.__doc__) >= 2)


if __name__ == '__main__':
    u.main()
