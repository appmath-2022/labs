import numpy as np

def HilbertМatrix(k):
    matrix = [[(1 / (i + j + 1)) for i in range(k)] for j in range(k)]
    return matrix

def matrixWithDiagonalDominance(k):
    matrix = np.random.randint(100, size=(k, k))

    for i in range(k):
        for j in range(k):
            if (i != j):
                a = matrix[i][i] / k
                matrix[i][j] = np.random.randint(-a, a)
    return matrix