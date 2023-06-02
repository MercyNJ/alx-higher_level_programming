#!/usr/bin/python3
"""Contains a matrix multiplication funct using Numpy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication result of two matrices.

    Args:
        m_a (list of lists of ints/floata): The 1st matrix.
        m_b (list of lists of ints/floata): The 2nd matrix.
    """

    return (np.matmul(m_a, m_b))
