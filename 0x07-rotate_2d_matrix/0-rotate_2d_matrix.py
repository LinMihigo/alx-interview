#!/usr/bin/python3
"""Task 0
"""


def rotate_2d_matrix(matrix):
    """Rotating matrix by 90 degrees clockwise
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Transpose
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()
