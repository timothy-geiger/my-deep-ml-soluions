import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(A[0]))
    x_cpy = np.zeros(len(A[0]))

    diag = np.diag(A)
    non_diag = A - np.diag(diag)

    for _ in range(n):
        for i in range(len(x)):
            x_cpy[i] = (1 / diag[i]) * (b[i] - sum(non_diag[i]*x))

        x = np.round(x_cpy.copy(), 4)

    return x


A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
n = 2

res = solve_jacobi(A, b, n)
print(res)
