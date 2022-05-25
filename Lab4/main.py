from jacobi import *
from test_matrixes import *
from matrix_build import *
from scipy.linalg import hilbert

print("Тест правильности решения метода на 100 случайных матрицах")
is_correct = True
for count in range(100):
    n = 10
    a = random_simmetric_matrix(n)
    # здесь находим собственные значения и векторы заданной матрицы
    # первый аргумент - сама матрица, второй - точность
    # возвращает лист собственных чисел и лист собственных векторов
    w, e, cnt = find_by_error(a, 0.1)
    for i in range(len(w)):
        eq = np.round(a.dot(e[i]) - w[i] * np.array(e[i]), 1)
        if not np.array_equal(eq, np.zeros([n, 1])):
            is_correct = False


print(f"Значения и векторы найдены корректно: {is_correct}")

print("Самодельные матрицы с диагональным преобладанием")
for i in [10, 50, 100, 500, 1000]:
    for n in [100]:

        print(f"k = {i}")
        matrixA = symmetrical_matrix_with_diagonal_dominance(i, n)

        print(f"Число обусловленности: {np.linalg.cond(matrixA)}")
        is_matrix_symmetrical = True
        has_diagonal_dominance = True
        for j in range(n):
            row_sum = 0
            for z in range(n):
                if z != j:
                    row_sum += abs(matrixA[j][z])
                if matrixA[z][j] != matrixA[j][z]:
                    is_matrix_symmetrical = False
            if abs(matrixA[j][j]) < row_sum:
                has_diagonal_dominance = False

        print(f"Матрица обладает диагональным преобладанием: {has_diagonal_dominance}")
        print(f"Матрица симметрична: {is_matrix_symmetrical}")
        if not is_matrix_symmetrical:
            break

        is_correct = True
        w, e, cnt = find_by_error(matrixA, 0.1)
        print("find by error done")
        w1, e1, error = find_by_iteration_limit(matrixA, cnt * 95 / 100)
        print("find by iteration limit done")
        for z in range(len(w)):
            eq = np.round(matrixA.dot(e[z]) - w[z] * np.array(e[z]), 1)
            if not np.array_equal(eq, np.zeros([n, 1])):
                is_correct = False
        if is_correct:
            print(f"Метод вращений решил правильно за {cnt} операций")
            print(f"Погрешность - {error}")
        else:
            print(f"Метод вращений решил НЕправильно.")


        print("-------------------------------------------------")

print("Матрицы Гильберта")
for n in [10, 50, 100]:

    print(f"k = {n}")
    matrixA = hilbert(n)

    print(f"Число обусловленности: {np.linalg.cond(matrixA)}")
    is_matrix_symmetrical = True
    for j in range(n):
        row_sum = 0
        for z in range(n):
            if matrixA[z][j] != matrixA[j][z]:
                is_matrix_symmetrical = False
    print(f"Матрица симметрична: {is_matrix_symmetrical}")
    if not is_matrix_symmetrical:
        break


    is_correct = True
    w, e, cnt = find_by_error(matrixA, 0.1)
    print("find by error done")
    w1, e1, error = find_by_iteration_limit(matrixA, cnt / 10)
    print("find by iteration limit done")
    for z in range(len(w)):
        eq = np.round(matrixA.dot(e[z]) - w[z] * np.array(e[z]), 1)
        if not np.array_equal(eq, np.zeros([n, 1])):
            is_correct = False
    if is_correct:
        print(f"Метод вращений решил правильно за {cnt} операций")
        print(f"Погрешность - {error}")
    else:
        print(f"Метод вращений решил НЕправильно.")

    print("-------------------------------------------------")