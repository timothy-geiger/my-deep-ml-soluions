import numpy as np


def ridge_loss(
        X: np.ndarray,
        w: np.ndarray,
        y_true: np.ndarray,
        alpha: float) -> float:
    mse = np.mean((y_true - X @ w) ** 2)
    reg_term = alpha * np.sum(w**2)

    return mse + reg_term
