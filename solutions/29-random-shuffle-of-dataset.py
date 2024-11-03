import numpy as np


def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)

    idx = np.arange(len(X))
    np.random.shuffle(idx)

    return X[idx], y[idx]


X = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]])
y = np.array([1, 2, 3, 4])

res = shuffle_data(X, y)
print(res)
