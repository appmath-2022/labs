import numpy as np


def add_variables(matrix, linear_form):
    m = matrix.shape[0]
    n = matrix.shape[1]
    linear_form = np.append(linear_form, np.zeros(m))
    basis = [i for i in range(n, n + m)]

    matrix = np.hstack([matrix, np.identity(m)])

    return matrix, linear_form, basis


def build_start_basis(matrix, basis):
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


def remove_negative_elements(matrix, basis):
    n = matrix.shape[1]
    m = matrix.shape[0]
    flag = True
    while not flag:
        flag = True

        for j in range(m):
            if matrix[0, j] < 0:
                flag = False
        if not flag:
            print("Убираем элементы")
            row = [0]
            # находим наибольший по модулю свободный элемент
            for i in range(m):
                if abs(matrix[i, 0]) > abs(matrix[row[0], 0]):
                    row = [i]
                # на случай, если есть два числа, одинаковых по модулю, но в одной строке будут отрицательные элементы,
                # а в другой - нет
                elif abs(matrix[i, 0]) == abs(matrix[row[0], 0]):
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
                if abs(matrix[row, j]) > abs(matrix[row, col]):
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


def transform_matrix(matrix, row, col):
    main_element = matrix[row, col]
    new_table = matrix.copy()
    for j in range(matrix.shape[1]):
        new_table[row, j] = matrix[row, j] / main_element
    for i in range(matrix.shape[0]):
        if i != row:
            for j in range(matrix.shape[1]):
                new_table[i, j] -= matrix[row, j] * matrix[i, col] / main_element

    return new_table


def add_linear_form(matrix, basis, linear_form):
    n = matrix.shape[1]
    last_line_simplex_matrix = np.array([])
    for i in range(n):
        tmp_sum = 0
        for j in range(len(linear_form)):
            if j + 1 in basis:
                tmp_sum += linear_form[j + 1] * matrix[basis.index(j + 1), i]
        last_line_simplex_matrix = np.append(last_line_simplex_matrix, -tmp_sum + linear_form[i])

    return np.append(matrix, [last_line_simplex_matrix], axis=0)


def check_ones(matrix: np.array):
    m = matrix.shape[0]
    n = matrix.shape[1]

    cover_basis = np.zeros(m - 1)

    for j in range(1, n):
        zeros = 0
        ones = 0
        last_one = -1
        for i in range(m - 1):
            if matrix[i, j] != 0 and matrix[i, j] != 1:
                continue
            if matrix[i, j] == 1:
                last_one = i
                ones += 1
            else:
                zeros += 1

        if zeros == m - 2 and ones == 1:
            cover_basis[last_one] = last_one + 1
    if len(np.where(cover_basis == 0)[0]) == 0:
        return True, cover_basis
    return False, cover_basis

