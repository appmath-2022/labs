import numpy as np
from decompositionLU import decomposition_lu


def solve(a, ans):
    l, u = decomposition_lu(a)
    return solve_lu(l, u, ans)


# решение методом Гаусса
def solve_lu(L, U, ans):
    n = L.shape[0]
    y = np.matrix(np.zeros([n, 1]))
    for i in range(n):
        y[i, 0] = ans[i, 0] - L[i, :i] * y[:i]

    x = np.matrix(np.zeros([n, 1]))
    for i in range(1, n + 1):
        x[-i, 0] = (y[-i] - U[-i, -i:] * x[-i:, 0]) / U[-i, -i]
    return x


def reverse(a):
    l, u = decomposition_lu(a)
    n = a.shape[0]
    reversed_matrix = np.matrix(np.zeros([n, n]))

    for i in range(n):
        ans = np.matrix(np.zeros([n, 1]))
        ans[i] = 1
        x = solve_lu(l, u, ans)

        for j in range(n):
            reversed_matrix[j, i] = x[j]

    return reversed_matrix


def jacobi(a, ans, max_iterations, accuracy):
    a = np.matrix(a)
    ans = np.matrix(ans)
    n = a.shape[0]
    d = np.matrix([[i] for i in np.diagonal(a)])

    x = np.zeros([n, 1])
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        nx = a * x - np.multiply(d, x) - ans
        nx = -np.divide(nx, d)
        current_error = max(abs(x - nx))
        if current_error < accuracy:

            return nx, iteration
        x = nx
    print("iteration limit")
    print(current_error)
    return x, iteration
