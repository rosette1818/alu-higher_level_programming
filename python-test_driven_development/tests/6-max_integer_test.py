#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_regular_list(self):
        """Ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """List with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """List of negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """List of negative and positive numbers"""
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument given, uses default (empty list)"""
        self.assertIsNone(max_integer())

    def test_all_same_values(self):
        """All values are the same"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_floats(self):
        """List containing floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
