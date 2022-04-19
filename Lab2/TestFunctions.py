import numpy as np


class SimpleParabola:
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
