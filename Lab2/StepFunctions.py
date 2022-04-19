import methods as m
import sympy


def ConstStep(iteration, f, grad, prev_x, a):
    if a == 0:
        a = 0.001  # дефолтное значение шага
    if iteration % 10 == 0:
        a *= 2
    while f(prev_x) <= f([prev_x[i] - a * grad[i] for i in range(len(prev_x))]):
        a /= 2
    return a


def StepSplit(iteration, f, grad, prev_x, a):
    e = 0.1
    if a == 0:
        a = 1  # дефолтное значение шага
    while f(prev_x) - f([prev_x[i] - a * grad[i] for i in range(len(prev_x))]) < e * a * sum([i ** 2 for i in grad]):
        a *= 0.95
    return a


def GoldenRatio(iteration, f, grad, prev_x, a):
    a = sympy.symbols('a')
    a1, a2, a3 = m.golden_ratio(sympy.lambdify(a, f([prev_x[i] - a * grad[i] for i in range(len(prev_x))])), 0, 10 ** 6, 0.1)
    return (a1 + a2) / 2


def Fibonacci(iteration, f, grad, prev_x, a):
    a = sympy.symbols('a')
    a1, a2, a3 = m.fibonacci(sympy.lambdify(a, f([prev_x[i] - a * grad[i] for i in range(len(prev_x))])), 0, 10 ** 6, 0.1)
    return (a1 + a2) / 2
