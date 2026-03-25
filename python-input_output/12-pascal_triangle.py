#!/usr/bin/python3
"""Module that contains a function returning Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    
    # We already have row 1, so loop from 1 to n-1
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1
        
        # Calculate the middle numbers by looking at the previous row
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
            
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
