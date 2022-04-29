import sys
import numpy as np


def decompositionLU(a):
    if 0 in a.diagonal():
        print("main diagonal contains zero elements", file=sys.stderr)
        return 0, 0

    n = a.shape[0]
    L = np.matrix(np.zeros([n, n]))
    U = np.matrix(np.zeros([n, n]))

    for k in range(n):
        for j in range(k, n):
            U[k, j] = a[k, j] - L[k, :k] * U[:k, j]
        for i in range(k, n):
            L[i, k] = (a[i, k] - L[i, : k] * U[: k, k]) / U[k, k]

    return L, U
