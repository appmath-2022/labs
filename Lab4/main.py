from jacobi import *
from test_matrixes import *
print("Тест правильности решения метода на 100 случайных матрицах")
is_correct = True
for count in range(100):
    n = 10
    a = random_simmetric_matrix(n)
    # здесь находим собственные значения и векторы заданной матрицы
    # первый аргумент - сама матрица, второй - точность
    # возвращает лист собственных чисел и лист собственных векторов
    w, e = find(a, 0.1)
    for i in range(len(w)):
        eq = np.round(a.dot(e[i]) - w[i] * np.array(e[i]), 1)
        if not np.array_equal(eq, np.zeros([n, 1])):
            is_correct = False

print(f"Значения и векторы найдены корректно: {is_correct}")
