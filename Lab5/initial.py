import numpy as np


def add_variables(matrix: np.ndarray, linear_form: list) -> (np.ndarray, list):
    """
     Функция, которая используется в случае использования симметричной формы задачи линейного программирования. Добавляет
    новые искусственные переменные в симплекс-таблицу и целевую функцию, чтобы скомпенсировать знаки неравенства
    :param matrix: Исходная симплекс-матрица
    :param linear_form: Исходная целевая функция
    :return: Новая симплекс-матрица, новая целевая функция
    """
    m = matrix.shape[0]
    n = matrix.shape[1]
    linear_form = np.append(linear_form, np.zeros(m))
    basis = [i for i in range(n, n + m)]

    matrix = np.hstack([matrix, np.identity(m)])

    return matrix, linear_form, basis


def build_start_basis(matrix: np.ndarray, basis: list) -> (np.ndarray, list):
    """
    Приводит симплекс-таблицу к единичному виду, выделяет базис, однако он необязательно должен быть опорным
    :param matrix: Исходная симплекс-матрица
    :param basis: Исходный базис(если есть). Если нет, нужно использовать просто пустой лист
    :return: Новая симплекс-матрица, новый базис
    """
    n = matrix.shape[1]
    m = matrix.shape[0]
    row = 0
    print("Строим начальный базис")
    while len(basis) != m:
        col = -1
        for j in range(1, n):
            if j not in basis:
                zeros = 0
                for i in range(m):
                    if matrix[i, j] == 0:
                        zeros += 1
                if zeros != m and matrix[row, j] != 0:
                    col = j
                    basis.append(col)
                    matrix = transform_matrix(matrix, row, col)
                    matrix = np.round(matrix, 10)
                    break
                if zeros == m - 1 and matrix[row, j] == 1:
                    basis.append(col)
        row += 1
    return matrix, basis


def remove_negative_elements(matrix: np.ndarray, basis: list) -> (np.ndarray, list):
    """
    Анализирует симплекс-матрицу на наличие отрицательных свободных членов. Если таковых нет, вернется исходная матрица.
    В противном случае отрицательные элементы будут удалены из матрицы, а базис перестроен.
    :param matrix: Исходная симплекс-матрица
    :param basis: Исходный базис
    :return: Новая симплекс-матрица, новый базис
    :exception: Данная задача линейного программирования не имеет решений
    """
    n = matrix.shape[1]
    m = matrix.shape[0]
    flag = False
    while not flag:
        flag = True

        for j in range(m):
            if matrix[j, 0] < 0:
                flag = False
        if not flag:
            print("Убираем элементы")
            row = [0]
            # находим наибольший по модулю свободный элемент
            for i in range(m):
                if matrix[i, 0] < matrix[row[0], 0]:
                    row = [i]
                # на случай, если есть два числа, одинаковых по модулю, но в одной строке будут отрицательные элементы,
                # а в другой - нет
                elif matrix[i, 0] == matrix[row[0], 0]:
                    row.append(i)

            is_negative_existed = False
            for r in row:
                for j in range(1, n):
                    if matrix[r, j] < 0:
                        is_negative_existed = True
                        row = r
                        break
            if not is_negative_existed:
                raise Exception("Нет решений")

            col = 1
            for j in range(1, n):
                if matrix[row, j] < matrix[row, col]:
                    col = j

            main_element = matrix[row, col]

            for j in range(n):
                matrix[row, j] /= main_element

            for i in range(m):
                if i != row:
                    for j in range(n):
                        matrix[i, j] -= matrix[row, j] * matrix[i, col]
            basis[row] = col
    return matrix, basis


def transform_matrix(matrix: np.ndarray, row: int, col: int) -> np.ndarray:
    """
    Непосредственно добавляет определенную переменную в базис
    :param matrix: Исходная симплекс-таблица.
    :param row: Строка, в которой содержится разрешающий элемент.
    :param col: Столбец, в котором содержится разрешающий элемент.
    :return: Новая симплекс-матрица
    """
    main_element = matrix[row, col]
    new_table = matrix.copy()
    for j in range(matrix.shape[1]):
        new_table[row, j] = matrix[row, j] / main_element
    for i in range(matrix.shape[0]):
        if i != row:
            for j in range(matrix.shape[1]):
                new_table[i, j] -= matrix[row, j] * matrix[i, col] / main_element

    return new_table


def add_linear_form(matrix: np.ndarray, basis: list, linear_form: list):
    """Добавляет в симплекс-таблицу целевую функцию. Целевая функция предварительно приводится к виду, соответствующему
    базисным переменным.
    :param matrix: Исходная симплекс-таблица.
    :param basis: Исходный базис.
    :param linear_form: Исходная целевая функция.
    :returns: Новая симплекс-матрица
    """
    n = matrix.shape[1]
    last_line_simplex_matrix = np.array([])
    for i in range(n):
        tmp_sum = 0
        for j in range(len(linear_form)):
            if j + 1 in basis:
                tmp_sum += linear_form[j + 1] * matrix[basis.index(j + 1), i]
        last_line_simplex_matrix = np.append(last_line_simplex_matrix, -tmp_sum + linear_form[i])

    return np.append(matrix, [last_line_simplex_matrix], axis=0)
