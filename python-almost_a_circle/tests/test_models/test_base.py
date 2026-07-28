#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_assigned(self):
        """Test that a given id is assigned directly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        """Test that ids auto-increment when not given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a populated list."""
        d = [{"id": 1}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        s = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1}])

    def test_save_and_load_file(self):
        """Test save_to_file and load_from_file for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 2)
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create_rectangle(self):
        """Test create for Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create for Square."""
        s1 = Square(5, 1, 2, 10)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_save_and_load_file_csv(self):
        """Test save_to_file_csv and load_from_file_csv for Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        squares = Square.load_from_file_csv()
        self.assertEqual(len(squares), 2)
        os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
