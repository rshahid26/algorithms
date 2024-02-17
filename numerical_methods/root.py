import random


def bisection(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        return "No guaranteed root on this interval"

    while abs(a - b) > epsilon:
        mid = (a + b) / 2

        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) > 0:
            # the midpoint has the same sign as a
            a = mid
        else:
            # the midpoint has the same sign as b
            b = mid

    return (a + b) / 2

def fpi(f, a, b, epsilon, max_iterations: int = 100_000):
    g = lambda x: x - f(x)

    x0 = random.uniform(a, b)
    i = 0
    while i < max_iterations:
        # move horizontally and vertically in cobweb diagram
        x1 = g(x0)
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1
        i += 1

def newton_raphson(f, dfdx, a, b, epsilon):
    x0 = random.uniform(a, b)

    while True:
        x1 = x0 - (f(x0) / dfdx(x0))
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1

def secant(f, a, b, epsilon):
    x0 = random.uniform(a, b)
    x1 = random.uniform(a, b)

    while abs(x1 - x0) >= epsilon:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2

    return x1