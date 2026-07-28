#!/usr/bin/python3
"""Module that divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of integers or floats.
        div: integer or float divisor.

    Returns:
        A new matrix with every element divided by div.

    Raises:
        TypeError: if matrix is not a list of lists of integers or
            floats, if the rows of matrix are not all the same size,
            or if div is not a number.
        ZeroDivisionError: if div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(n, (int, float)) for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
