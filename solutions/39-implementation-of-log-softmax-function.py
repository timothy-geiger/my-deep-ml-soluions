import numpy as np


def log_softmax(scores: list) -> np.ndarray:
    scores = scores - np.max(scores)
    tmp = np.log(np.sum(np.exp(scores)))

    return scores - tmp
