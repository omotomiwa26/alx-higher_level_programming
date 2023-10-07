#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
    # Test if it returns the maximum number in the given list
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([5, 6, 7, 8]), 8)
        self.assertAlmostEqual(max_integer([-2.0, 6.8, 7.5, -8.2]), 7.5)
        self.assertAlmostEqual(max_integer([-2.0, 6, 7, 8.9]), 8.9)
        self.assertAlmostEqual(max_integer(['layi', 'wasabi', 'is', 'funny']), 'wasabi')
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(['layi']), 'layi')
        self.assertAlmostEqual(max_integer(''), None)
        self.assertAlmostEqual(max_integer('layi'), 'y')
        self.assertAlmostEqual(max_integer([5, 6, 8, 8]), 8)
    

    #def test_values(self):
        # Test if it raises value error when wrong values are used in the list
        # self.assertRaises(TypeError, max_integer, (['1', '2', '3', '4']))
