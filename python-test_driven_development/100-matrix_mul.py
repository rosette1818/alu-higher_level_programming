#!/usr/bin/python3
"""Module for lazy_matrix_mul function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        ndarray: Resulting matrix multiplication.
    """
    return np.matmul(m_a, m_b)
