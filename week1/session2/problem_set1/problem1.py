"""
Problem 1: Transpose Matrix

Write a function transpose() that accepts a 2D integer array matrix and 
returns the transpose of matrix. The transpose of a matrix is the matrix 
flipped over its main diagonal, swapping the rows and columns.

Example Usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

Example Output:
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
[
    [1, 4],
    [2, 5],
    [3, 6]
]
"""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []

    for i in range(len(matrix[0])):
        row: list[int] = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)

    return res


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose(matrix))
