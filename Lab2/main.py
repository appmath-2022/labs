import numpy as np
import ConjugateGradientMethod
import methods
import TestFunctions
import matplotlib.pyplot as plt


def sliding_window_method(investigated_function):
    h = 0.01
    a0 = 0
    while not ((investigated_function(a0 - h) > investigated_function(a0)) & (
            investigated_function(a0 + h) > investigated_function(a0))):
        if investigated_function(a0 + h) > investigated_function(a0):
            a0 = a0 - h / 2
        else:
            a0 = a0 + h / 2
    return a0


investigated_function_object = TestFunctions.SimpleParabola
result, number_of_iterations = ConjugateGradientMethod.proceed(
    gradient=investigated_function_object.gradient,
    function=investigated_function_object.function,
    error=0.0005,
    minimization_method=methods.golden_ratio,
    x=investigated_function_object.x,
    x_previous=investigated_function_object.x_previous,
    extrema_finding_function=sliding_window_method
)
minimum_coords = result[len(result) - 1]
print(f"Координаты точки минимума {minimum_coords}")
print(f"Минимальное значение функции: {investigated_function_object.function(minimum_coords)}")
print(f"Количество итераций: {number_of_iterations}")
fig, axes = plt.subplots(nrows=1, ncols=1)

axes.contour(*investigated_function_object.args, investigated_function_object.function(investigated_function_object.args), 10)
axes.plot(*np.array(result).T)
plt.show()
