import numpy as np


def proceed(gradient, function, error, x, x_previous, minimization_method, extrema_finding_function):
    direction = np.zeros(len(x))
    beta = 0
    counter = 0
    track = []

    while np.linalg.norm(x - x_previous) > error:
        counter += 1
        direction = (-gradient(x) + beta * direction) / np.linalg.norm(-gradient(x) + beta * direction)

        def f(a):
            return function(x + a * direction)

        result = minimization_method(f, 0, extrema_finding_function(f), error)
        alpha = (result[0] + result[1]) / 2
        x_previous = x
        track.append(x)
        x = x + alpha * direction
        beta = np.dot(gradient(x), gradient(x) - gradient(x - x_previous)) / np.linalg.norm(x_previous) ** 2

    return [track, counter]
