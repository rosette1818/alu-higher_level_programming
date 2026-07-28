#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices of integers or floats using numpy.

    Args:
        m_a: list of lists of integers or floats.
        m_b: list of lists of integers or floats.

    Returns:
        A numpy.ndarray, the product of m_a and m_b.

    Raises:
        TypeError: if m_a or m_b is not a list, not a list of lists,
            contains elements that are not integers or floats, or
            has rows of different sizes.
        ValueError: if m_a or m_b is empty, or if they can't be
            multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not all(isinstance(n, (int, float)) for n in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(n, (int, float)) for n in row):
            raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
