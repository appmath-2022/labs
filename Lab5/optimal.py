import numpy as np


def optimize(matrix_b: list, matrix_d: np.ndarray, max_n_iter: int) -> (np.ndarray, np.ndarray):
    """
    Находит оптимальный план по опорному
    :param matrix_b: Базис после поиска опорного плана.
    :param matrix_d: Симплекс-таблица
    :param: max_n_iter: Максимальное количество итераций
    :return: Решенная симплекс-таблица, оптимальный план
    """
    n = matrix_d.shape[1]
    m = matrix_d.shape[0]
    counter = 0
    while not is_end(matrix_d) and counter < max_n_iter:
        main_col = find_main_col(matrix_d)
        main_row = find_main_row(matrix_d, main_col)
        matrix_b[main_row] = main_col
        new_table = np.zeros((m, n))
        for i in range(n):
            new_table[main_row, i] = matrix_d[main_row, i] / matrix_d[main_row, main_col]
        for i in range(m):
            if i != main_row:
                for j in range(n):
                    new_table[i, j] = matrix_d[i, j] - matrix_d[i, main_col] * new_table[main_row, j]
        matrix_d = new_table
        counter += 1
    result = np.zeros(n - 1)
    for i in range(n - 1):
        k = matrix_b.index(i + 1) if i + 1 in matrix_b else -1
        if k != -1:
            result[i] = matrix_d[k, 0]
    return matrix_d, result


def is_end(matrix_d: np.ndarray) -> bool:
    """
    Проверяет симплекс-таблицу на оптимальность (поиск минимума)
    :param matrix_d: симплекс-таблица
    :return: True, если план оптимален, False в обратном случае
    """
    n = matrix_d.shape[1]
    m = matrix_d.shape[0]
    for i in range(1, n):
        if matrix_d[m - 1, i] > 0:
            return False
    return True


def find_main_col(matrix_d: np.ndarray) -> int:
    """
    Находит разрешающей столбец симплекс-матрицы.
    :param matrix_d: симплекс-матрица
    :return: индекс разрешающего столбца
    """
    elements = matrix_d[-1, 1:]
    max_e = np.amax(elements, axis=0)
    col = np.where(elements == max_e)[0]
    return col + 1


def find_main_row(matrix_d: np.ndarray, main_col: int) -> int:
    """
    Находит разрешающую строку.
    :param matrix_d: симплекс-матрица
    :param main_col: текущий разрешающий столбец
    :return: индекс разрешающей строки

    :exception Бросает базовое исключение, если функция не ограничена на заданной области, то есть задача не имеет решений
    """
    row = 0
    m = matrix_d.shape[0]
    for i in range(m - 1):
        if matrix_d[i, main_col] != 0:
            if matrix_d[i, 0] / matrix_d[i, main_col] > 0:
                row = i
                break

    if row == 0 and matrix_d[0, 0] / matrix_d[0, main_col] <= 0:
        raise Exception("Функция не ограничена на заданной области")

    for i in range(m - 1):
        if matrix_d[i, main_col] != 0:
            if matrix_d[i, 0] / matrix_d[i, main_col] > 0:
                if matrix_d[i, 0] / matrix_d[i, main_col] <= matrix_d[row, 0] / matrix_d[row, main_col]:
                    row = i

    return row
