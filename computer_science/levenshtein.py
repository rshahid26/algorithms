def levenshtein_distance(x: str, y: str) -> int:
    """
    Returns the Levenshtein distance between two strings x and y.
    Allowed operations with cost=1: insertions, deletions, replacements.
    """
    # Bottom-Up DP. O(mn) time, O(min(m, n)) space
    m, n = len(x), len(y)
    back = [n - i for i in range(n + 1)]

    for i in range(m - 1, -1, -1):
        front = [0] * (n + 1)
        front[-1] = 1 + back[-1]

        for j in range(n - 1, -1, -1):
            if x[i] == y[j]:
                front[j] = back[j + 1] # Keep character
            else:
                front[j] = 1 + min(front[j + 1], back[j + 1], back[j])
        back = front
        
    return back[0]

def levenshtein_matrix(x: str, y: str) -> list:
    """
    Returns the levenshtein distance of all substrings x[i:] and y[j:]
    in an mxn matrix dp where m = len(x) and n = len(y).
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Exhausted x, insert remaining n-j characters y[j:]
    for j in range(n + 1):
        dp[m][j] = n - j
    # Base case: Exhausted y, delete remaining m-i characters x[i:]
    for i in range(m + 1):
        dp[i][n] = m - i

    # Bottom-Up DP. O(mn) time, O(mn) space
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):

            if x[i] == y[j]:
                dp[i][j] = dp[i + 1][j + 1] # Keep character
            else:
                dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
    return dp


def levenshtein_sequence(x: str, y: str) -> list:
    """
    Returns a list of intermediate strings z_i where each z_i+1 is the
    result of applying the ith Levenshtein distance operation to z_i.
    """
    m, n = len(x), len(y)
    dp = levenshtein_matrix(x, y)

    sequence = [x]
    def traverse(i, j, z):
        if i == m and j == n:
            return
        
        if j != n and dp[i][j] == 1 + dp[i][j + 1]:
            z = z[:i] + y[j] + z[i:] # Insert y[j]
            sequence.append(z)
            traverse(i, j + 1, z)
        elif i != m and dp[i][j] == 1 + dp[i + 1][j]:
            z = z[:i] + z[i + 1:] # Delete x[i]
            sequence.append(z)
            traverse(i + 1, j, z)
        elif i != m and j != n and dp[i][j] == 1 + dp[i + 1][j + 1]:
            z = z[:i] + y[j] + z[i + 1:] # Replace x[i] with y[j]
            sequence.append(z)
            traverse(i + 1, j + 1, z)
        else:
            traverse(i + 1, j + 1, z)
    
    traverse(0, 0, x)
    return sequence