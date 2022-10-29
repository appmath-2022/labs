import numpy as np


def solve(matrix_b, matrix_d):
    n = matrix_d.shape[1]
    m = matrix_d.shape[0]
    while not is_end(matrix_d, n, m):
        main_col = find_main_col(matrix_d, n, m)
        main_row = find_main_row(matrix_d, main_col, m)
        matrix_b[main_row] = main_col
        new_table = np.zeros((m, n))
        for i in range(n):
            new_table[main_row, i] = matrix_d[main_row, i] / matrix_d[main_row, main_col]
        for i in range(m):
            if i != main_row:
                for j in range(n):
                    new_table[i, j] = matrix_d[i, j] - matrix_d[i, main_col] * new_table[main_row, j]
        matrix_d = new_table
    result = np.zeros(n - 1)
    for i in range(n - 1):
        k = matrix_b.index(i + 1) if i + 1 in matrix_b else -1
        if k != -1:
            result[i] = matrix_d[k, 0]
    return matrix_d, result


# все коэффициенты должны стать неположительными
def is_end(matrix_d, n, m):
    for i in range(1, n):
        # если есть хотя бы один положительный, то идем дальше
        if matrix_d[m - 1, i] > 0:
            return False
    return True


# поиск разрешающего столбца
# наибольший элемент - положительный - так как мы прошли проверку на виток цикла
# берем максимальный элемент среди положительных в строчке с коэффициентами линейной формы
def find_main_col(matrix_d, n, m) -> int:
    col = 1

    for i in range(2, n):
        if matrix_d[m - 1, i] > matrix_d[m - 1, col]:
            col = i
    return col


# выбираем минимальный положительный элемент из разрешающего столбца
def find_main_row(matrix_d, main_col, m) -> int:
    row = 0
    # проверка на то, есть ли вообще хотя бы один положительный элемент
    for i in range(m - 1):
        if matrix_d[i, main_col] > 0:
            row = i
            break

    if row == 0 and matrix_d[0, main_col] <= 0:
        raise Exception("Функция не ограничена на заданной области")

    for i in range(m - 1):
        if matrix_d[i, main_col] > 0:
            if matrix_d[i, 0] / matrix_d[i, main_col] <= matrix_d[row, 0] / matrix_d[row, main_col]:
                row = i

    return row


def show_matrix(matrix):
    for i in matrix:
        for s in i:
            print(s, end="\t")
        print()
