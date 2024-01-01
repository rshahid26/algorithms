def dirichlet_approximation(real_num, epsilon):
    """
    Approximates any real number using integer values p, q where
    p / q is within "epsilon" distance of the real number.

    Uses Dirichlet's Approximation Theorem to find the qth multiple of
    the real number within 1/qN of the nearest integer. q's existence
    is guaranteed by the pigeonhole principle.
    """
    limit = round(1 / epsilon)
    fractionals = []

    while True:
        for i in range(limit):
            fractionals.append((real_num * i) % 1)

        for i in range(limit):
            for j in range(i + 1, limit + 1):
                if abs(fractionals[i] - fractionals[j]) < abs(i - j) / limit:
                    return [round((j - i) * real_num), j - i]

        limit += 1
        fractionals = []
