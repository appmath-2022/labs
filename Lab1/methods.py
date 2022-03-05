from math import sqrt


def dichotomy(function, left_border, right_border, error):
    a = left_border
    b = right_border
    iteration_counter = 0
    number_digits_after_comma = len(str(error).split('.')[1]) + 1  # количество знаков после запятой

    while round(abs(b - a), number_digits_after_comma) > error:
        x1 = (a + b) / 2.0 - error / 2.0
        x2 = (a + b) / 2.0 + error / 2.0

        if function(x1) < function(x2):
            b = x2
        else:
            a = x1

        iteration_counter += 1

    return a, b, iteration_counter


def golden_ratio(function, left_border, right_border, error):
    a = left_border
    b = right_border
    iteration_counter = 0
    number_digits_after_comma = len(str(error).split('.')[1]) + 1  # количество знаков после запятой

    phi = (3 - sqrt(5)) / 2

    x1 = a + phi * (b - a)
    x2 = b - phi * (b - a)

    first_value = function(x1)
    second_value = function(x2)

    while round(abs(b - a), number_digits_after_comma) > error:
        if first_value > second_value:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            first_value = second_value
            second_value = function(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            second_value = first_value
            first_value = function(x1)

        iteration_counter += 1

    return [a, b, iteration_counter]


def fibonacci(function, left_border, right_border, error):
    return NotImplementedError
