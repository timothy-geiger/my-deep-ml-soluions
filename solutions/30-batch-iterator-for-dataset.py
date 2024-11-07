import math
import numpy as np


def batch_iterator(X, y=None, batch_size=64):
    res = []

    for i in range(math.ceil(len(X)/batch_size)):
        res.append([])
        start, end = i*batch_size, i*batch_size+batch_size

        if y is not None:
            res[-1] = [X[start:end], y[start:end]]

        else:
            res[-1] = X[start:end]
    return res


X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2

res = batch_iterator(X, y, batch_size)
print(res)
