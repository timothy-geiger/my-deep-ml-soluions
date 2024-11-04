import numpy as np
import math


def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)  # -> not used because checking for unique result

    rows = len(data)
    sub_size = math.ceil(rows / k)

    folds = [
        [
            np.concatenate(
                (data[:i*sub_size], data[i*sub_size+sub_size:]), axis=0
            ).tolist(),
            data[i*sub_size:i*sub_size+sub_size].tolist(),
        ]
        for i in range(k)
    ]

    # Your code here
    return folds


data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
k = 5

res = cross_validation_split(data, k)
print(res)
