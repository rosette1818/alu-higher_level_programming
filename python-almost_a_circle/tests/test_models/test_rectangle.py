#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_attributes(self):
        """Test that attributes are set correctly."""
        r = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test width raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_value_error(self):
        """Test width raises ValueError when not > 0."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_x_type_error(self):
        """Test x raises TypeError on non-int."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_y_value_error(self):
        """Test y raises ValueError when < 0."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with key-worded arguments."""
        r = Rectangle(10, 10, 10, 10)
        rid = r.id
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/3 - 4/2".format(rid))

    def test_to_dictionary(self):
        """Test to_dictionary output."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
