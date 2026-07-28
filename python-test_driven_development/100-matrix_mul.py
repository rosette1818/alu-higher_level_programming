#!/usr/bin/python3
"""Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: list of lists of ints/floats
        m_b: list of lists of ints/floats

    Returns:
        list of lists: the product matrix

    Raises:
        TypeError: for various invalid matrix inputs
        ValueError: if matrices are empty or can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError("m_b should contain only integers or floats")
    a_row_len = len(m_a[0])
    for row in m_a:
        if len(row) != a_row_len:
            raise TypeError("each row of m_a must be of the same size")
    b_row_len = len(m_b[0])
    for row in m_b:
        if len(row) != b_row_len:
            raise TypeError("each row of m_b must be of the same size")
    if a_row_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
