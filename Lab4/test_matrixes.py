import numpy as np


def random_simmetric_matrix(n: int) -> np.array:
    matrix = np.random.randint(-1000, 1000, size=(n, n))

    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = matrix[j][i]

    return matrix
