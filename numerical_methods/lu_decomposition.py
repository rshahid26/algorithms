import numpy as np

def lu_decomposition(A):
    """
    Decomposes a matrix A into a lower-triangular matrix L,
    upper-triangular matrix U, and a permutation matrix P
    such that PA=LU. Returns L, U, P.
    """
    n = A.shape[0]
    U = A.copy().astype(float)
    L = np.eye(n, dtype=float)
    P = np.eye(n, dtype=float)

    for i in range(n):
        # Swap max column elements to the pivot for numerical stability
        max_index = np.argmax(np.abs(U[i:n, i])) + i
        if i != max_index:
            U[i], U[max_index] = U[max_index], U[i]
            P[i], P[max_index] = P[max_index], P[i]

        # Perform Gaussian elimination on U = PA to make it upper-triangular
        for j in range(i + 1, n):
            scalar = U[j, i] / U[i, i]
            U[j, i:] -= scalar * U[i, i:]
            # Record E_i to compose the lower-triangular matrix L
            L[j, i] = scalar

    return L, U, P
