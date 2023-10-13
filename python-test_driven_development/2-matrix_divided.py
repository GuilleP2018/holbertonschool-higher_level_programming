#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """>>> matrix_divided([[]], 3)
[[]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], -2)
[[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]
>>> matrix_divided([[1.5, 2.8, 3.3], [4.2, 5.5, 6.6]], 2)
[[0.75, 1.4, 1.65], [2.1, 2.75, 3.3]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if type(div) is float:
        div = round(div, 2)
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
