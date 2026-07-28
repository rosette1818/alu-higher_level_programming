#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_square_basic(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual((s.size, s.x, s.y), (1, 0, 0))

    def test_square_with_x(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_square_with_xy(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_attributes(self):
        """Test that attributes are set correctly."""
        s = Square(5, 1, 3, 12)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test_too_many_args(self):
        """Test Square with too many positional arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_type_error(self):
        """Test Square("1") raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_type_error(self):
        """Test Square(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        """Test Square(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Test area calculation."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_to_dictionary(self):
        """Test to_dictionary output."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

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

    def test_size_type_error_setter(self):
        """Test size raises TypeError on non-int."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update_args_none(self):
        """Test update() with no arguments."""
        s = Square(5)
        s.update()
        self.assertEqual(s.size, 5)

    def test_update_args_id(self):
        """Test update(89)."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_args_size(self):
        """Test update(89, 1)."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_args_x(self):
        """Test update(89, 1, 2)."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_args_full(self):
        """Test update(89, 1, 2, 3)."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwargs_id(self):
        """Test update(id=89)."""
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)

    def test_update_kwargs_size(self):
        """Test update(id=89, size=1)."""
        s = Square(5)
        s.update(id=89, size=1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_x(self):
        """Test update(id=89, size=1, x=2)."""
        s = Square(5)
        s.update(id=89, size=1, x=2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_full(self):
        """Test update(id=89, size=1, x=2, y=3)."""
        s = Square(5)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_kwargs_id(self):
        """Test Square.create(id=89)."""
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)

    def test_create_kwargs_size(self):
        """Test Square.create(id=89, size=1)."""
        s = Square.create(id=89, size=1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_kwargs_x(self):
        """Test Square.create(id=89, size=1, x=2)."""
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_kwargs_full(self):
        """Test Square.create(id=89, size=1, x=2, y=3)."""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_list(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"size": 1', content)
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        s1 = Square(5, 1, 2)
        Square.save_to_file([s1])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(str(squares[0]), str(s1))
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
