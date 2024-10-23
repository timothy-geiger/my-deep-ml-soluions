def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:

    if len(a[0]) != len(b):
        return -1

    res = [0] * len(b)

    for i in range(len(a)):
        for j in range(len(b)):
            res[i] += a[i][j] * b[j]

    return res
