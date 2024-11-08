import numpy as np


def to_categorical(x, n_col=None):
    n_col = np.max(x) + 1 if n_col is None else n_col

    res = np.zeros((len(x), n_col))
    res[np.arange(len(x)), x] = 1

    return res
