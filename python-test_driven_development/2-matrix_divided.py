#!/usr/bin/python3
"""Module for dividing all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of ints/floats
        div: int or float divisor

    Returns:
        list of lists: new matrix with divided elements

    Raises:
        TypeError: if matrix is not a valid matrix of ints/floats,
            if rows are not the same size, or if div is not a number
        ZeroDivisionError: if div is 0
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(err_matrix)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
