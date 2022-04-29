import numpy as np
from decompositionLU import decompositionLU


def solve(a, ans):
    l, u = decompositionLU(a)
    return solveLU(l, u, ans)


def solveLU(L, U, ans):
    n = L.shape[0]
    y = np.matrix(np.zeros([n, 1]))
    for i in range(y.shape[0]):
        y[i, 0] = ans[i, 0] - L[i, :i] * y[:i]

    x = np.matrix(np.zeros([n, 1]))
    for i in range(1, n + 1):
        x[-i, 0] = (y[-i] - U[-i, -i:] * x[-i:, 0]) / U[-i, -i]
    return x


def reverse(a):
    l, u = decompositionLU(a)
    n = a.shape[0]
    a1 = np.matrix(np.zeros([n, n]))
    for i in range(n):
        ans = np.matrix(np.zeros([n, 1]))
        ans[i] = 1
        x = solveLU(l, u, ans)
        for j in range(n):
            a1[j, i] = x[j]
    return a1


def jacobi(a, ans, max_iterations, accuracy):
    n = a.shape[0]
    d = np.matrix([[i] for i in np.diagonal(a)])
    x = np.zeros([n, 1])
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        nx = a * x - np.multiply(d, x) - ans
        nx = -np.divide(nx, d)
        if max(abs(x - nx)) < accuracy:
            return nx, iteration
        x = nx
    return x, iteration
