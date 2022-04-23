import numpy as np
import math
import sympy


class UnrealSimpleParabola:
    x = np.array([10, 10])
    x_previous = np.array([100, 100])
    x_axe = np.meshgrid(-10, 10, 0.1)
    y_axe = np.meshgrid(-10, 10, 0.1)
    args = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1))

    @staticmethod
    def gradient(argument_list):
        return np.array([2 * argument_list[0] - 10, 0])

    @staticmethod
    def function(argument_list):
        return (argument_list[0] - 5) ** 2


class AnotherSimpleParabola:
    x = np.array([10, 10])
    x_previous = np.array([100, 100])
    x_axe = np.meshgrid(-10, 10, 0.1)
    y_axe = np.meshgrid(-10, 10, 0.1)
    args = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1))

    @staticmethod
    def gradient(argument_list):
        return np.array([2 * argument_list[0], 4 * argument_list[1]])

    @staticmethod
    def function(argument_list):
        return argument_list[0] ** 2 + 2 * argument_list[1] ** 2


class function1:
    x = np.array([1, 1])
    x_previous = np.array([100, 100])
    x_axe = np.meshgrid(-1, 1, 0.01)
    y_axe = np.meshgrid(-1, 1, 0.01)
    args = np.meshgrid(np.arange(-0.25, 1.75, 0.01), np.arange(-1, 1, 0.01))

    @staticmethod
    def gradient(argument_list):
        return np.array([4 * argument_list[0] - 3, 6 * argument_list[1]])

    @staticmethod
    def function(argument_list):
        return 2 * argument_list[0] ** 2 + 3 * argument_list[1] ** 2 - 3 * argument_list[0]


class function2:
    x = np.array([10, 10])
    x_previous = np.array([100, 100])
    x_axe = np.meshgrid(-10, 10, 0.01)
    y_axe = np.meshgrid(-10, 10, 0.01)
    args = np.meshgrid(np.arange(-10, 10, 0.01), np.arange(-10, 10, 0.01))

    @staticmethod
    def gradient(argument_list):
        return np.array(
            [0.52 * argument_list[0] - 0.48 * argument_list[1], 0.52 * argument_list[1] - 0.48 * argument_list[0]])

    @staticmethod
    def function(argument_list):
        return 0.26 * (argument_list[0] ** 2 + argument_list[1] ** 2) - 0.48 * argument_list[0] * argument_list[1]


class function3:
    x = np.array([15, 20])
    x_previous = np.array([100, 100])
    x_axe = np.meshgrid(-20, 20, 0.01)
    y_axe = np.meshgrid(-20, 20, 0.01)
    args = np.meshgrid(np.arange(-20, 20, 0.01), np.arange(-20, 20, 0.01))

    @staticmethod
    def gradient(argument_list):
        return np.array([2 * argument_list[0] + 2 * argument_list[1], 2 * argument_list[0] + 6 * argument_list[1]])

    @staticmethod
    def function(argument_list):
        return argument_list[0] ** 2 + 2 * argument_list[0] * argument_list[1] + 3 * argument_list[1] ** 2
