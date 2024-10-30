import math


def sigmoid(z: float) -> float:
    res = 1 / (1 + math.exp(-z))

    return round(res, 4)


res = sigmoid(0.0)
print(res)
