# python-test_driven_development

Test-driven development exercises in Python using `doctest` and
`unittest`.

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two integers (floats are cast to int). |
| `2-matrix_divided.py` | Divides all elements of a matrix by a divisor. |
| `3-say_my_name.py` | Prints `My name is <first_name> <last_name>`. |
| `4-print_square.py` | Prints a square using the `#` character. |
| `5-text_indentation.py` | Prints text with new lines after `.`, `?`, `:`. |
| `6-max_integer.py` | Finds the max integer in a list. |
| `100-matrix_mul.py` | Multiplies two matrices. |
| `101-lazy_matrix_mul.py` | Multiplies two matrices using NumPy. |

Tests live in the `tests/` folder and are run with:

```
python3 -m doctest ./tests/*.txt
python3 -m unittest tests.6-max_integer_test
```
