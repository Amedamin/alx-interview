#!/usr/bin/python3
"""
Rotate the given N x N 2D MATRIX 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(MATRIX):
    """
    Rotates a given 2D MATRIX 90 degrees clockwise.
    """
    N = len(MATRIX)
    # Rotate the MATRIX layer by layer
    for I in range(N // 2):
        for J in range(I, N - I - 1):
            # Perform the 4-way exchange
            TEMP = MATRIX[I][J]
            MATRIX[I][J] = MATRIX[N - J - 1][I]
            MATRIX[N - J - 1][I] = MATRIX[N - I - 1][N - J - 1]
            MATRIX[N - I - 1][N - J - 1] = MATRIX[J][N - I - 1]
            MATRIX[J][N - I - 1] = TEMP
