from GradientDescent import gradient_descent
import StepFunctions as Sf


def function1(x):
    return 10 * x[0] ** 2 + x[1] ** 2  # use only sympy or build-in functions


def gradient(x):
    return [20 * x[0], 2 * x[1]]


if __name__ == '__main__':
    print(gradient_descent([10, 10], function1, gradient, 0.00001, Sf.const_step))

    print(gradient_descent([10, 10], function1, gradient, 0.00001, Sf.step_split))

    print(gradient_descent([10, 10], function1, gradient, 0.00001, Sf.golden_ratio))

    print(gradient_descent([10, 10], function1, gradient, 0.00001, Sf.fibonacci))
