import datetime

import numpy as np
import scipy.sparse as sp
from decompositionLU import decomposition_lu
from solutions import solve, reverse, jacobi
from math import sqrt
from matrixBuild import \
    hilbert_matrix, matrix_with_diagonal_dominance, matrix_f


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
    l, u = decomposition_lu(b)
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
    rand_ans = sp.rand(n, n, 1).multiply(
        10 ** 6).floor()
    x, iteration_number = jacobi(test, test_ans, n, 0.0001)
    if np.array_equal(np.around(test * x - test_ans, 3), np.zeros([3, 1])):
        print("solved correctly in", iteration_number, "iterations")
    else:
        print("solved incorrectly")
    iteration_limit = 100
    for n in [10, 50, 100, 500,1000]:
        for i in [1000]:

            print(f"k = {i}")
            matrixA = matrix_with_diagonal_dominance(i, n)
            matrixF = matrix_f(n, matrixA)

            # print("matrix built")
            print(f"Число обусловленности: {np.linalg.cond(matrixA)}")
            isnorm = True
            for j in range(n):
                summ = 0
                for z in range(n):
                    if z != j:
                        summ += abs(matrixA[j][z])
                if abs(matrixA[j][j]) < summ:
                    isnorm = False
            print(isnorm)

            # true_result = solve(matrixA, matrixF)

            result, iteration_number = jacobi(matrixA, matrixF, iteration_limit, 0.001)

            eq = matrixA * result - matrixF

            error = sqrt(sum([e ** 2 for e in eq]))
            print(f"Погрешность {error}")


            if np.array_equal(np.round(eq, 3), np.zeros([n, 1])):
                print(f"SOLVED in {iteration_number}")



            # eq = np.around(matrixA * true_result - matrixF, 3)
            #
            # if np.array_equal(eq, np.zeros([i, 1])):
            #     print(f"SOLVED")


            print("-------------------------------------------------")

    # for n in [10, 50, 100, 500, 1000]:
    #     print(f"n = {n}")
    #     matrixA = hilbert_matrix(n)
    #     matrixF = matrix_f(n, matrixA)
    #
    #     print(f"Число обусловленности: {np.linalg.cond(matrixA)}")
    #     isnorm = True
    #     for j in range(n):
    #         summ = 0
    #         for z in range(n):
    #             if z != j:
    #                 summ += abs(matrixA[j, z])
    #         if abs(matrixA[j, j]) < summ:
    #             isnorm = False
    #     print(isnorm)
    #
    #     true_result = solve(matrixA, matrixF)
    #
    #     result, iteration_number = jacobi(matrixA, matrixF, iteration_limit, 0.001)
    #
    #     eq = matrixA * result - matrixF
    #
    #     error = sqrt(sum([e ** 2 for e in eq]))
    #     print(f"Погрешность {error}")
    #
    #     if np.array_equal(np.round(eq, 3), np.zeros([n, 1])):
    #         print(f"SOLVED in {iteration_number}")
    #
    #
    #     eq = np.around(matrixA * true_result - matrixF, 3)
    #
    #     if np.array_equal(eq, np.zeros([n, 1])):
    #         print(f"SOLVED")
    #
    #     print("-------------------------------------------------")

    for n in [10, 50, 100, 500, 1000, 10 ** 4]:
        print(f"n = {n}")
        matrixA = matrix_with_diagonal_dominance(100, n)
        matrixF = matrix_f(n, matrixA)
        timer = datetime.datetime.now()
        true_result = solve(matrixA, matrixF)
        print(datetime.datetime.now() - timer)
        timer = datetime.datetime.now()

        result, iteration_number = jacobi(matrixA, matrixF, iteration_limit, 0.0001)
        print(datetime.datetime.now() - timer)

        eq = matrixA * result - matrixF

        if np.array_equal(np.round(eq, 1), np.zeros([n, 1])):
            print(f"SOLVED in {iteration_number}")

        eq = np.around(matrixA * true_result - matrixF, 3)

        if np.array_equal(eq, np.zeros([n, 1])):
            print(f"SOLVED")

        print("-------------------------------------------------")