import numpy as np


def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    tr = sum([matrix[i][i] for i in range(len(matrix))])
    det = np.linalg.det(matrix)

    eigenvalues = [
        np.round((tr/2) + np.sqrt((tr/2)**2 - det), 4),
        np.round((tr/2) - np.sqrt((tr/2)**2 - det), 4)
    ]

    return eigenvalues


res = calculate_eigenvalues(
    matrix=[[2, 1], [1, 2]]
)

print(res)
