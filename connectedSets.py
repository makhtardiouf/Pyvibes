#!/usr/bin/env python3

"""
Connected sets

"""

def countConnects(matrix):
    visited = {}
    h = len(matrix)
    count = 0
    for i, row in enumerate(matrix):
        b = len(row)
        for j, item in enumerate(row):
            if isVisitable(matrix, i, j, b, h, visited):
                count += 1
                searchDepth(matrix, i, j, b, h, visited)
    return count


def isVisitable(matrix, i, j, b, h, visited):
    if i >= 0 and j >= 0 and i < b and j < h:
        if (i, j) not in visited and matrix[i][j] == 1:
            return True


def searchDepth(matrix, i, j, b, h, visited):
    # Surrounding box: N , W , E , S , NE , NW , SE , SW directions
    box = ((-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)
                )

    if isVisitable(matrix, i, j, b, h, visited):
        for s in box:
            visited[(i, j)] = 1
            searchDepth(matrix, i + s[0], j + s[1], b, h, visited)

matrix = [[1, 1, 0, 0, 0],
       [0, 1, 0, 0, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]
       ]

print countConnects(matrix)
