import numpy as np


def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    # Min-Max
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)

    normalized_data = (data - min_val) / (max_val - min_val)

    return np.round(standardized_data, 4), np.round(normalized_data, 4)


res = feature_scaling(
    data=np.array([[5.4, 4.4], [1.3, 2.4], [6.9, 3.3]])
)

print(res)
