import numpy as np


def make_diagonal(x):
    identity = np.identity(len(x))
    return identity*x


x = np.array([1, 2, 3])
res = make_diagonal(x)

print(res)
