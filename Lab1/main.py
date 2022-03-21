import math as m
import methods


def investigated_function(x):
    return m.sin(x) * pow(x, 3)


if __name__ == "__main__":
    a, b, n = methods.dichotomy(investigated_function, 4, 6, 0.0005)
    print(a, b, n)
    print(a-b)

    a, b, n = methods.golden_ratio(investigated_function, 4, 6, 0.0005)
    print(a, b, n)
    print(a-b)

    a, b, n = methods.fibonacci(investigated_function, 4, 6, 0.0005)
    print(a, b, n)
    print(a-b)

    a, b, n = methods.parabola(investigated_function, 4, 6, 0.0005)
    print(a, b, n)
    print(a - b)

    a, b, n = methods.brent(investigated_function, 4, 6, 0.0005)
    print(a, b, n)
    print(a - b)

