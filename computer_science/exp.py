def exp(x: float, n: int) -> float:
    """
    Raise a number x to an integer power n using a divide and
    conquer algorithm with T(n) = T(floor(n/2)) + O(1) = O(logn)
    time complexity.
    """
    if n == 0 or x == 1:
        return 1

    def exp_recursive(x: float, n: int):
        if n == 1:
            return x
        if n % 2 == 0:
            return exp_recursive(x * x, n // 2)
        else:
            return x * exp_recursive(x * x, n // 2)

    res = exp_recursive(x, abs(n))
    return res if n >= 0 else 1 / res