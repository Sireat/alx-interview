#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    '''
    Function to find Pascal's Triangle integers

        Parameters:
            n (int): The number of row's of Pascal's triangle

        Returns:
            pascal_triangle (list): Binary string of the sum of a and b
    '''
    pascal_triangle = list()

    if n <= 0:
        return pascal_triangle

    # Add first 1.
    if n > 0:
        pascal_triangle.append([1])

    # Add second line.
    if n > 1:
        pascal_triangle.append([1, 1])

    for x in range(3, n+1):
        pascal_triangle.append([0] * x)

        # Set first and last 1
        pascal_triangle[x-1][0] = 1
        pascal_triangle[x-1][x-1] = 1

        # Calculate middle numbers
        for y in range(1, x-1):
            pascal_triangle[x-1][y] = \
                pascal_triangle[x-2][y-1] + pascal_triangle[x-2][y]

    return pascal_triangle
