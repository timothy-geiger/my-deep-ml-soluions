def calculate_covariance_matrix(
        vectors: list[list[float]]) -> list[list[float]]:

    m, n = len(vectors), len(vectors[0])
    covariance_matrix = [[0.0 for _ in range(m)] for _ in range(m)]
    means = [sum(feature) / n for feature in vectors]

    for x in range(m):
        for y in range(x, m):
            covariance = 0

            for i in range(n):
                covariance += \
                    (vectors[x][i] - means[x]) * (vectors[y][i] - means[y])

            covariance = covariance / (n - 1)
            covariance_matrix[x][y] = covariance_matrix[y][x] = covariance

    return covariance_matrix


A = [[1, 2, 3], [4, 5, 6]]

res = calculate_covariance_matrix(A)
print(res)
