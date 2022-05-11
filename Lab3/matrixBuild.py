import numpy as np


def hilbert_matrix(k):
    matrix = [[(1 / (i + j + 1)) for i in range(k)] for j in range(k)]
    return np.matrix(matrix)


def matrix_with_diagonal_dominance(k, n):
    matrix = np.random.uniform(-100, 100, size=(n, n))
    for i in range(n):
        if matrix[i][i] == 0:
            matrix[i][i] = n

    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = matrix[i][i] / (k * 1.0) * np.random.randint(-n, n + 1)
        matrix[i][i] *= n ** 2

    return matrix


def matrix_f(n, matrix):
    x = np.arange(n)
    x = [[i + 1] for i in x]
    return matrix.dot(x)  # Возвращает матрицу F из условия
