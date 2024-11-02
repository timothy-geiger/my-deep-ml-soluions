import numpy as np 


def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    U = A.T @ A
    theta = 0.5 * np.arctan2(2 * U[0, 1], U[0, 0] - U[1, 1])
    j = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]])

    A_prime = j.T @ U @ j
    res = np.sqrt(np.diag(A_prime))

    return j, res, j.T


res = svd_2x2_singular_values(np.array([[2, 1], [1, 2]]))
print(res)
