import math
import numpy as np


def single_neuron_model(
    features: list[list[float]],
    labels: list[int],
    weights: list[float],
    bias: float
) -> (list[float], float):

    probas = []
    n = len(labels)

    for feature_vec in features:
        z = sum(w*f for w, f in zip(weights, feature_vec)) + bias
        prob = 1 / (1 + math.exp(-z))
        probas.append(round(prob, 4))

    mse = sum((prob-label)**2 for prob, label in zip(probas, labels)) / n
    mse = round(mse, 4)

    return probas, mse


features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1

res = single_neuron_model(features, labels, weights, bias)
print(res)
