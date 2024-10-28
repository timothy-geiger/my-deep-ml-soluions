import numpy as np


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    return (1/det)*np.array([
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]])


matrix = [[4, 7], [2, 6]]
res = inverse_2x2(matrix)

print(res)
