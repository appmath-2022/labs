from GradientDescent import GradientDescent
import StepFunctions as Sf


def function1(x):
    return 10 * x[0] ** 2 + x[1] ** 2  # use only sympy or build-in functions


def gradient(x):
    return [20 * x[0], 2 * x[1]]


if __name__ == '__main__':
    print(GradientDescent([10, 10], function1, gradient, 0.00001, Sf.ConstStep))
    #
    # print(GradientDescent([10, 10], function1, gradient, 0.00001, Sf.StepSplit))
    #
    # print(GradientDescent([10, 10], function1, gradient, 0.00001, Sf.GoldenRatio))

    print(GradientDescent([10, 10], function1, gradient, 0.00001, Sf.Fibonacci))
