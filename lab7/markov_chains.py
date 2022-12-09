import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as linalg


def read() -> np.ndarray:
    file = open("matrix.txt", "r")
    matrix = [[float(num) for num in line.split(',')] for line in file]
    matrix = np.array(matrix)
    epsilon = 1e-6
    correct_matrix = True
    for i in range(matrix.shape[0]):
        line_sum = 0
        for j in range(matrix.shape[1]):
            line_sum += matrix[i][j]
        if abs(line_sum - 1) > epsilon:
            correct_matrix = False
    if not correct_matrix:
        print("Your matrix is incorrect")
        return
    return matrix


def numerical_solution(matrix: np.ndarray) -> np.ndarray:
    if matrix is None:
        return
    index = np.random.randint(0, matrix.shape[0] - 1)
    pred_vector = matrix[index]

    pred_vector = np.array(pred_vector)
    vector = pred_vector.dot(matrix)
    epsilon = 0.00001
    iteration = 0
    iteration_limit = 1e2
    iterations = []
    deviations = []

    while abs(np.std(pred_vector - vector) >= epsilon) and iteration < iteration_limit:
        iteration += 1
        pred_vector = vector
        vector = vector.dot(matrix)

        iterations.append(iteration)
        deviations.append(np.std(vector))

    plt.plot(iterations, deviations)
    plt.title(index)
    plt.show()
    return vector


def analytical_solution(matrix: np.ndarray) -> np.ndarray:
    if matrix is None:
        return
    eigenvalues, left_eigenvectors = linalg.eig(matrix, right=False, left=True)
    vector = left_eigenvectors[:, 0]
    vector_norm = [x/np.sum(vector).real for x in vector]
    return vector_norm
