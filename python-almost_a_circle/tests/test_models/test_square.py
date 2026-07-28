#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_attributes(self):
        """Test that attributes are set correctly."""
        s = Square(5, 1, 3, 12)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_size_getter(self):
        """Test the size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        """Test size raises TypeError on non-int."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        self.assertEqual(s.id, 1)

    def test_update_kwargs(self):
        """Test update with key-worded arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary output."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
