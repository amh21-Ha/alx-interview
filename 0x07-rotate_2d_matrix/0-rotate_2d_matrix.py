#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """a method to rotate 2D matrix 90 degrees clockwise"""
    N = len(matrix)
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = temp
