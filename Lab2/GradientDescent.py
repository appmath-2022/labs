def GradientDescent(x, f, d, accuracy, step):
    iteration = 0
    prev_x = [i + 1 for i in x]  # + 2 * accuracy
    a = 0
    trajectory = [x]
    while abs(f(x) - f(prev_x)) >= accuracy:
        iteration += 1
        prev_x = x
        grad = d(x)
        a = step(iteration, f, grad, prev_x, a)
        x = [x[i] - a * grad[i] for i in range(len(x))]
        trajectory.append(x)
        if a == 0:
            return x, iteration, trajectory
    return x, iteration, trajectory
