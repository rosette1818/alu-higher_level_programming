#!/usr/bin/python3
"""Module for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.

    Args:
        m_a: list of lists of ints/floats
        m_b: list of lists of ints/floats

    Returns:
        numpy.ndarray: the product matrix
    """
    return np.matmul(m_a, m_b)
