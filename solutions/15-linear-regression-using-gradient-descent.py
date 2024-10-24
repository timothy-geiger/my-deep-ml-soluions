import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:

    m, n = X.shape
    theta = np.zeros((n, 1))

    for _ in range(iterations):
        preds = X @ theta
        err = preds - y.reshape(-1, 1)
        theta -= alpha * (X.T @ err) / m

    return np.round(theta.flatten(), 4)


res = linear_regression_gradient_descent(
    X=np.array([[1, 1], [1, 2], [1, 3]]),
    y=np.array([1, 2, 3]),
    alpha=0.01,
    iterations=1000,
)

print(res)
