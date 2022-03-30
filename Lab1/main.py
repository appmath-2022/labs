import math as m
import methods


def investigated_function(x):
    return m.sin(x) * pow(x, 3)


def function1(x):
    return 5 * m.cos(x) + pow(x, 2)


def function2(x):
    return x * x - x + 1


def test(function, left, right, error):
    print(left, ' ', right, ' ', error)
    print("dichotomy")
    a, b, n = methods.dichotomy(function, left, right, error)
    print(a, b, n)

    print("golden ratio")
    a, b, n = methods.golden_ratio(function, left, right, error)
    print(a, b, n)

    print("fibonacci")
    a, b, n = methods.fibonacci(function, left, right, error)
    print(a, b, n)

    print("parabola")
    a, b, n = methods.parabola(function, left, right, error)
    print(a, b, n)

    print("brent")
    a, b, n = methods.brent(function, left, right, error)
    print(a, b, n)

    print('\n')


if __name__ == "__main__":
    test(investigated_function, 4, 6, '0.005')
    test(investigated_function, 4, 6, '0.0005')
    test(investigated_function, 4, 6, '0.00005')

    test(function1, 1, 4, '0.005')
    test(function1, 1, 4, '0.0005')
    test(function1, 1, 4, '0.00005')

    test(function2, -1, 2, '0.005')
    test(function2, -1, 2, '0.0005')
    test(function2, -1, 2, '0.00005')



