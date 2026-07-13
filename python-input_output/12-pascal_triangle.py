#!/usr/bin/python3
"""Module that defines the pascal_triangle function."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing the triangle,
            or an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
