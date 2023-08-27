def misra_gries(a: list, k: int) -> list:
    """Generalization of Boyer-Moore algorithm.
    Returns elements that appear more than N * 1/k times"""

    m = [None] * (k - 1)
    counter = [0] * (k - 1)

    for element in a:
        for i, candidate in enumerate(m):
            if element == m[i] or counter[i] == 0:
                m[i] = element
                counter[i] += 1
                break
        else:
            counter = [count - 1 for count in counter]

    solutions = []
    for majority in m:
        if a.count(majority) > len(a) // k:
            solutions.append(majority)

    return solutions

# a = [1, 5, 1, 1, 6, 3, 5, 1, 3, 3]  # length 9