#!/usr/bin/python3
"""
This module contains the pascal_triangle function
"""

def pascal_triangle(n):
    """
    function to return a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): width of triangle

    Returns:
        list of lists: if n <= 0, returns empty list
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
