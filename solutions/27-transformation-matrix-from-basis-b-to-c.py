import numpy as np


def transform_basis(
        B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    C_inv = np.linalg.inv(np.array(C))

    return np.round(C_inv @ np.array(B), 4)


B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C = [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]]

res = transform_basis(B, C)
print(res)
