"""
Problem 1: Matrix Addition

Write a function add_matrices() that accepts two n x m matrices 
matrix1 and matrix2. The function should return an n x m matrix 
sum_matrix that is the sum of the given matrices such that each 
value in sum_matrix is the sum of values of corresponding elements 
in matrix1 and matrix2.

Example Usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

add_matrices(matrix1, matrix2)

Example Output:
[
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]
"""


def add_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    return []


if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print(add_matrices(matrix1, matrix2))
