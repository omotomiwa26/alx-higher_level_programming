#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        # Test if returns the maximum number in the given list
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([5, 6, 7, 8]), 8)
        self.assertAlmostEqual(max_integer([]), None)

    #def test_values(self):
        # Test if it raises value error when wrong values are used in the list
        # self.assertRaises(TypeError, max_integer, (['1', '2', '3', '4']))
