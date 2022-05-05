import numpy as np
import scipy.sparse as sp
from decompositionLU import decompositionLU
from solutions import solve, reverse, jacobi
from matrixBuild import HilbertМatrix, matrixWithDiagonalDominance


def initialize_test_matrix():  # разреженно-строчный формат
    indptr = np.array([0, 3, 6, 9, 11, 13, 16, 19, 23, 28, 31])
    indices = np.array([0, 4, 5, 1, 4, 8, 2, 3, 7, 3, 9, 4, 8, 5, 7, 9, 2, 6, 8, 1, 5, 7, 9, 0, 4, 6, 8, 9, 1, 3, 9])
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4])
    return sp.csr_matrix((data, indices, indptr), shape=(10, 10))


if __name__ == '__main__':
    a = initialize_test_matrix()
    n = 100
    # lu test
    b = sp.rand(n, n, 1).multiply(
        10 ** 6).floor()  # Генерирует рандомную матрицу. Первые 2 элементы размеры, 3 плотность
    l, u = decompositionLU(b)
    if np.array_equal(np.around(l * u - b, 3), np.zeros([n, n])):
        print("lu found correctly")
    # solver test
    ans = sp.rand(n, 1, 1).multiply(10 ** 6).floor()
    x = solve(b, ans)
    if np.array_equal(np.around(b * x - ans, 3), np.zeros([n, 1])):
        print("solved correctly")
    # reverser test
    if np.array_equal(np.around(reverse(b) * b, 3), np.eye(n)):
        print("reversed correctly")
    # iteration solver test
    test = np.matrix([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
    test_ans = np.matrix([[20], [33], [36]])
    x, iter = jacobi(test, test_ans, n, 0.0001)
    if np.array_equal(np.around(test * x - test_ans, 3), np.zeros([3, 1])):
        print("solved correctly in", iter, "iterations")