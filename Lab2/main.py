import numpy as np
import ConjugateGradientMethod as cg
import methods as m
import TestFunctions as tf
import matplotlib.pyplot as plt
import StepFunctions as sf
import GradientDescent as gd


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


def decoration_output(res):
    print(f"Координаты точки минимума {res[0]}")
    print(f"Количество итераций: {res[1]}")
    previous_coords = [1 for i in range(len(res[2]))]
    counter = 1
    arr = []
    for i in res[2]:
        relation = abs(np.mean([i[j] / previous_coords[j] for j in range(len(i))]))
        previous_coords = i
        print(f"Итерация {counter}: {i}, отношение {relation}")
        arr.append(relation)
        counter += 1
    print(f"Средняя скорость сходимости: {np.mean(arr)}")
    print()


funct_obj = tf.AnotherSimpleParabola

print("Пункт 1 - 2. Сравнение скорости сходимости метода в зависимости от метода поиска величины шага")
print("-----------------------------------------------------")
print("Постоянная величина шага")
result = gd.gradient_descent([10, 10], funct_obj.function, funct_obj.gradient, 0.00001, sf.const_step)
decoration_output(result)

print("Дробление шага")
result = gd.gradient_descent([10, 10], funct_obj.function, funct_obj.gradient, 0.00001, sf.step_split)
decoration_output(result)

print("Золотое сечение")
result = gd.gradient_descent([10, 10], funct_obj.function, funct_obj.gradient, 0.00001, sf.golden_ratio)
decoration_output(result)

print("Фибоначчи")
result = gd.gradient_descent([10, 10], funct_obj.function, funct_obj.gradient, 0.00001, sf.fibonacci)
decoration_output(result)

print("-----------------------------------------------------")

print("Пункт 5 - 6. Сравнение методов сопряженных градиентов и градиентного спуска")
func_obj = tf.SimpleParabola
result, number_of_iterations = cg.proceed(
    gradient=func_obj.gradient,
    function=func_obj.function,
    error=0.0005,
    minimization_method=m.golden_ratio,
    x=func_obj.x,
    x_previous=func_obj.x_previous,
    extrema_finding_function=sliding_window_method
)
print("-----------------------------------------------------")

minimum_coords = result[len(result) - 1]
print("Метод сопряженных градиентов")
print(f"Координаты точки минимума {minimum_coords}")
print(f"Минимальное значение функции: {func_obj.function(minimum_coords)}")
print(f"Количество итераций: {number_of_iterations}")
fig, axes = plt.subplots(nrows=1, ncols=1)

axes.contour(*func_obj.args,
             func_obj.function(func_obj.args), 10)
axes.plot(*np.array(result).T, label='Метод сопряженных градиентов')

minimum_coords, iteration_number, result = gd.gradient_descent(func_obj.x,
                                                               func_obj.function,
                                                               func_obj.gradient,
                                                               0.0005,
                                                               sf.golden_ratio
                                                               )
print("-----------------------------------------------------")
print("Метод градиентного спуска")
print(f"Координаты точки минимума {minimum_coords}")
print(f"Минимальное значение функции: {func_obj.function(minimum_coords)}")
print(f"Количество итераций: {number_of_iterations}")
axes.plot(*np.array(result).T, label='Метод градиентного спуска')
axes.legend()
plt.show()
