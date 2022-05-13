import numpy as np


def hilbert_matrix(k):
    matrix = [[(1 / (i + j + 1)) for i in range(k)] for j in range(k)]
    return np.matrix(matrix)


def matrix_with_diagonal_dominance(k, n):
    matrix = np.random.uniform(-n ** 3, n ** 3, size=(n, n))
    for i in range(n):
        if matrix[i][i] == 0:
            matrix[i][i] = np.random.randint(1, n ** 3)

    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = matrix[i][i] / (k * 1.0) * np.random.randint(-n ** 2, n ** 2 + 1)
        matrix[i][i] *= k ** 2

    return matrix


def random_tridiagonal_matrix(n):
    matrix = np.random.uniform(-n ** 3, n ** 3, size=(n, n))

    for i in range(n):
        for j in range(n):
            if j > i + 1 or j < i - 1:
                matrix[i][j] = 0
            if j == i - 1 or j == i + 1:
                matrix[i][j] /= n **2
    return matrix


def matrix_f(n, matrix):
    x = np.arange(n)
    x = [[i + 1] for i in x]
    return matrix.dot(x)  # Возвращает матрицу F из условия

