#!/usr/bin/env bash
set -e
mkdir -p python-almost_a_circle/models python-almost_a_circle/tests/test_models
cd python-almost_a_circle
cat > models/__init__.py << 'PYEOF_models___init___py'
PYEOF_models___init___py
cat > models/base.py << 'PYEOF_models_base_py'
#!/usr/bin/python3
"""Defines the Base class."""
import json
import csv


class Base:
    """Base class that manages the id attribute for all future classes.

    This class is the base of all other classes in this project and
    avoids duplicating the same id-management code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A string representing a list of dicts.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is None:
                list_objs = []
            for obj in list_objs:
                d = obj.to_dictionary()
                writer.writerow([d[field] for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class name>.csv."""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                list_dicts = []
                for row in reader:
                    d = {f: int(v) for f, v in zip(fields, row)}
                    list_dicts.append(d)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
PYEOF_models_base_py
cat > models/rectangle.py << 'PYEOF_models_rectangle_py'
#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, validating type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, validating type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate, validating type and value."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate, validating type and value."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character #."""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or key-worded arguments.

        Args:
            *args (ints): New attribute values in order id, width,
                height, x, y.
            **kwargs (dict): New attribute values by key/value.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
PYEOF_models_rectangle_py
cat > models/square.py << 'PYEOF_models_square_py'
#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, applying it to both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or key-worded arguments.

        Args:
            *args (ints): New attribute values in order id, size, x, y.
            **kwargs (dict): New attribute values by key/value.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
PYEOF_models_square_py
cat > tests/__init__.py << 'PYEOF_tests___init___py'
PYEOF_tests___init___py
cat > tests/test_models/__init__.py << 'PYEOF_tests_test_models___init___py'
PYEOF_tests_test_models___init___py
cat > tests/test_models/test_base.py << 'PYEOF_tests_test_models_test_base_py'
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
PYEOF_tests_test_models_test_base_py
cat > tests/test_models/test_rectangle.py << 'PYEOF_tests_test_models_test_rectangle_py'
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
PYEOF_tests_test_models_test_rectangle_py
cat > tests/test_models/test_square.py << 'PYEOF_tests_test_models_test_square_py'
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
PYEOF_tests_test_models_test_square_py
cat > README.md << 'PYEOF_README_md'
# python-almost_a_circle

Part of the ALU Higher Level Programming curriculum.

This project reviews core Python OOP concepts (classes, inheritance,
private attributes, getters/setters, class/static methods, `*args`
and `**kwargs`) and file/JSON/CSV serialization, building up the
`Base`, `Rectangle`, and `Square` classes.

## Layout

```
python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
└── README.md
```

## Usage

```
$ python3 -m unittest discover tests
```

## Author

Rosette
PYEOF_README_md
chmod +x models/*.py tests/*.py tests/test_models/*.py
echo "Project created in $(pwd)"
