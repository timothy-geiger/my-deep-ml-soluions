import numpy as np


def euclidean_distance(a, b):
    return np.sqrt(((a-b)**2).sum(axis=1))


def k_means_clustering(
    points: list[tuple[float, float]],
    k: int,
    initial_centroids: list[tuple[float, float]],
    max_iterations: int,
) -> list[tuple[float, float]]:
    points = np.array(points)
    centroids = np.array(initial_centroids)

    for _ in range(max_iterations):
        distances = np.array(
            [euclidean_distance(points, centroid)
                for centroid in initial_centroids]
        )

        min_clusters = np.argmin(distances, axis=0)

        new_centroids = np.array(
            [
                points[min_clusters == i].mean(axis=0)
                if len(points[min_clusters == i]) > 0
                else centroids[i]
                for i in range(k)
            ]
        )

        # check stopping criteria
        if np.all(centroids == new_centroids):
            return centroids

        centroids = np.round(new_centroids, 4)

    return centroids


points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)]
k = 2
initial_centroids = [(1, 1), (10, 1)]
max_iterations = 1

res = k_means_clustering(points, k, initial_centroids, max_iterations)
print(res)
