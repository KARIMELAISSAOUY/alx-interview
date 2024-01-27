#!/usr/bin/python3
"""
Module for 2D Matrix Rotation.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise

    Args:
        matrix (list): n x n. Matrix to rotate
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
                    
