from math import sqrt, copysign


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

    return a, b, iteration_counter


def fibonacci(function, left_border, right_border, error):
    fibonacci_numbers = [0, 1]
    last_fibonacci_number = 1
    n = 2
    while last_fibonacci_number < (right_border - left_border) / error:
        fibonacci_numbers.append(last_fibonacci_number)
        n += 1
        last_fibonacci_number = fibonacci_numbers[n - 1] + fibonacci_numbers[n - 2]
    fibonacci_numbers.append(last_fibonacci_number)
    n += 1
    a = left_border
    b = right_border

    d = error / 2

    x1 = a + fibonacci_numbers[n - 3] / fibonacci_numbers[n - 1] * (b - a)
    x2 = a + fibonacci_numbers[n - 2] / fibonacci_numbers[n - 1] * (b - a)

    first_value = function(x1)
    second_value = function(x2)

    k = 1

    while k != n:
        if first_value > second_value:
            a = x1
            x1 = x2
            x2 = a + fibonacci_numbers[n - 2 - k] / fibonacci_numbers[n - k - 1] * (b - a)
            first_value = second_value
            second_value = function(x2)

            if k == n - 2:
                x2 = x1 + d
                first_value = function(x1)
                second_value = function(x2)

                if first_value > second_value:
                    a = x1
                else:
                    b = x1
                break
            else:
                k += 1
        else:
            b = x2
            x2 = x1
            x1 = a + fibonacci_numbers[n - k - 3] / fibonacci_numbers[n - k - 1] * (b - a)
            second_value = first_value
            first_value = function(x1)

            if k == n - 2:
                x2 = x1 + d
                first_value = function(x1)
                second_value = function(x2)

                if first_value > second_value:
                    a = x1
                else:
                    b = x1
                break
            else:
                k += 1
    return a, b, k


def parabola(function, left_border, right_border, error):
    x1 = left_border
    x3 = right_border
    iteration_counter = 0
    number_digits_after_comma = len(str(error).split('.')[1]) + 1  # количество знаков после запятой

    while round(abs(x3 - x1), number_digits_after_comma) > error:

        x2 = (x1 + x3) / 2
        f1 = function(x1)
        f2 = function(x2)
        f3 = function(x3)

        u = x2 - ((x2 - x1) * (x2 - x1) * (f2 - f3) - (x2 - x3) * (x2 - x3) * (f2 - f1)) / (2 * ((x2 - x1) * (f2 - f3) -
                                                                                                 (x2 - x3) * (f2 - f1)))

        if u < x2:
            x3 = x2
        else:
            x1 = x2

        iteration_counter += 1

    return x1, x3, iteration_counter


def brent(function, left_border, right_border, error):
    a = left_border
    c = right_border
    phi = (3 - sqrt(5)) / 2
    x = w = v = (a + c) / 2
    fx = fw = fv = function(x)
    d = e = c - a
    iteration_counter = 0
    number_digits_after_comma = len(str(error).split('.')[1]) + 1
    while round(abs(c - a), number_digits_after_comma) > error:
        iteration_counter += 1
        g = e
        e = d
        u_temp = c
        if x != w and fx != fw and x != v and fx != fv and v != w and fv != fw:
            temp = [x, v, w]
            temp.sort()
            x1 = temp[0]
            x2 = temp[1]
            x3 = temp[2]
            f1 = function(x1)
            f2 = function(x2)
            f3 = function(x3)
            u_temp = x2 - ((x2 - x1) * (x2 - x1) * (f2 - f3) - (x2 - x3) * (x2 - x3) * (f2 - f1)) / (
                    2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        if a + error <= u_temp <= c - error and abs(u_temp - x) < g / 2:
            u = u_temp
            d = abs(u - x)
        else:
            if x < (c + a) / 2:
                u = x + phi * (c - x)
                d = c - x
            else:
                u = x - phi * (x - a)
                d = x - a
        fu = function(u)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
    return a, c, iteration_counter
