def get_pascals_triangle(numRows: int):
    memo = [[0] * (i + 1) for i in range(numRows)]

    def choose(n: int, k: int):
        if k == 0 or k == n:
            return 1
        elif memo[n][k] != 0:
            return memo[n][k]
        else:
            return choose(n - 1, k) + choose(n - 1, k - 1)

    for n in range(0, numRows):
        for k in range(0, n + 1):
            memo[n][k] = choose(n, k)

    return memo
