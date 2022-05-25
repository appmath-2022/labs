import numpy as np
from math import sqrt, atan, sin, cos, pi

from numpy import ndarray


def quad_sum_of_items_out_diagonal(matrix: ndarray) -> float:
    items_sum = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                items_sum += matrix[i][j] ** 2

    return sqrt(items_sum)


def create_rotation_matrix(matrix, i: int, j: int, n: int) -> ndarray:
    rotation_matrix = np.eye(n)
    if matrix[i][i] == matrix[j][j]:
        phi = pi / 4
    else:
        phi = 1 / 2 * atan((2 * matrix[i][j]) / (matrix[i][i] - matrix[j][j]))

    rotation_matrix[i][j] = -sin(phi)
    rotation_matrix[j][i] = sin(phi)
    rotation_matrix[i][i] = cos(phi)
    rotation_matrix[j][j] = cos(phi)

    return rotation_matrix


# работает только на симметрических матрицах потому что методичка
def find_by_error(matrix: ndarray, error: float):
    rotation_matrix = None
    n = len(matrix)
    cnt = 0

    tmp_matrix = matrix.copy()
    the_collection_of_eigenvectors = np.eye(n)

    while quad_sum_of_items_out_diagonal(tmp_matrix) > error:
        cnt += 1
        max_item = 0
        max_i = -1
        max_j = -1
        for i in range(n):
            for j in range(n):
                if i != j:
                    if abs(max_item) < abs(tmp_matrix[i][j]):
                        max_item = tmp_matrix[i][j]
                        max_i = i
                        max_j = j

        rotation_matrix = create_rotation_matrix(tmp_matrix, max_i, max_j, n)
        the_collection_of_eigenvectors = the_collection_of_eigenvectors.dot(rotation_matrix)

        tmp_matrix = rotation_matrix.T.dot(tmp_matrix).dot(rotation_matrix)

    the_collection_of_eigenvectors = the_collection_of_eigenvectors.T
    the_collection_of_eigenvectors = [[[j] for j in i] for i in the_collection_of_eigenvectors]
    return tmp_matrix.diagonal(), the_collection_of_eigenvectors, cnt



def find_by_iteration_limit(matrix: ndarray, iteration_limit: int):
    rotation_matrix = None
    n = len(matrix)

    tmp_matrix = matrix.copy()
    the_collection_of_eigenvectors = np.eye(n)
    cnt = 0

    while cnt < iteration_limit:
        cnt += 1
        max_item = 0
        max_i = -1
        max_j = -1
        for i in range(n):
            for j in range(n):
                if i != j:
                    if abs(max_item) < abs(tmp_matrix[i][j]):
                        max_item = tmp_matrix[i][j]
                        max_i = i
                        max_j = j

        rotation_matrix = create_rotation_matrix(tmp_matrix, max_i, max_j, n)
        the_collection_of_eigenvectors = the_collection_of_eigenvectors.dot(rotation_matrix)

        tmp_matrix = rotation_matrix.T.dot(tmp_matrix).dot(rotation_matrix)

    current_error = quad_sum_of_items_out_diagonal(tmp_matrix)
    the_collection_of_eigenvectors = the_collection_of_eigenvectors.T
    the_collection_of_eigenvectors = [[[j] for j in i] for i in the_collection_of_eigenvectors]
    return tmp_matrix.diagonal(), the_collection_of_eigenvectors, current_error



