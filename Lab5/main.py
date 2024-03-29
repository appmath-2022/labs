import numpy as np
import optimal
import initial

# Формат входного файла
# Вид экстремума: min либо max
# Целевая функция: коэффициенты через пробел перед всеми переменными, включая свободный член
# Ограничения: на каждой строчке одно ограничение, коэффициенты перед всеми переменными через пробел,
# знак равенства/неравенства ставить не нужно

file = open("input.txt", "r")

lines = [i.strip() for i in file.readlines()]
start_size = 0
extr_type = lines[0]
is_adding_needed = False
simplex_table = []
for line in lines[2:]:
    words = line.split()

    if words[-2] == "<=":
        is_adding_needed = True
        simplex_table.append([float(i) for i in words[:-2]] + [float(words[-1])])
    elif words[-2] == ">=":
        is_adding_needed = True
        simplex_table.append([-float(i) for i in words[:-2]] + [-float(words[-1])])
    else:
        simplex_table.append([float(i) for i in words[:-2]] + [float(words[-1])])
    simplex_table[-1].insert(0, simplex_table[-1][-1])
    simplex_table[-1].pop()
if extr_type == 'min':
    linear_form = [-float(i) for i in lines[1].split()]
    linear_form.insert(0, linear_form[-1])
    linear_form.pop()
    start_size = len(linear_form) - 1
elif extr_type == 'max':
    linear_form = [float(i) for i in lines[1].split()]
    linear_form.insert(0, linear_form[-1])
    linear_form.pop()
    start_size = len(linear_form) - 1
else:
    raise Exception("Некорректный формат ввода ы")
simplex_table = np.array(simplex_table)

try:
    if is_adding_needed:
        simplex_table, linear_form, start_basis = initial.add_variables(simplex_table, linear_form)
    else:
        start_basis = []

    simplex_table, start_basis = initial.build_start_basis(simplex_table, start_basis)

    print("Проверяем на наличие отрицательных переменных среди свободных членов")
    # проверка опорного плана на оптимальность
    simplex_table, start_basis = initial.remove_negative_elements(simplex_table, start_basis)
    # построение дельт
    print("Выражаем целевую функцию через начальные базисные переменные")
    simplex_table = initial.add_linear_form(simplex_table, start_basis, linear_form)
    print("Ищем оптимальный план")
    simplex_table, result = optimal.optimize(start_basis, simplex_table)
    print("Оптимальный план:")
    print(result[:start_size])
    print("Значение функции:")
    if lines[1] == 'min':
        print(-np.array(linear_form[1:]).dot(result.T) + linear_form[0])
    else:
        print(np.array(linear_form[1:]).dot(result.T) + linear_form[0])
except Exception as e:
    print(f"Возникла ошибка: {e}")
