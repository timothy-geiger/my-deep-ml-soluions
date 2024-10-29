def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    if len(a[0]) != len(b):
        return -1

    for i in range(len(a)):
        for j in range(len(b[1])):
            tmp = 0

            for k in range(len(a[0])):
                tmp += a[i][k]*b[k][j]

            res[i][j] = tmp

    return res


A = [[1, 2], [2, 4]]
B = [[2, 1], [3, 4]]

res = matrixmul(A, B)
print(res)
