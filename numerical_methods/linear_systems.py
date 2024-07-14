import numpy as np
from .lu_decomposition import lu_decomposition
def solve(A, b):
    """
    Solves a system of linear equations Ax = b using Gaussian
    Elimination. Returns the solution vector x.
    """
    A, b = np.array(A, dtype=float), np.array(b, dtype=float)
    n = len(A)

    # Forward elimination
    for i in range(n):
        pivot = A[i][i]
        for j in range(i + 1, n):
            scalar = -A[j][i] / pivot
            A[j, i:] += scalar * A[i, i:]
            b[j] += scalar * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x

def solve_lu(A, b):
    """
    Solve a system of linear equations Ax = b using LU
    decomposition with partial pivoting. Returns the solution
    vector x.
    """
    A, b = np.array(A, float), np.array(b, float)
    n = A.shape[0]
    L, U, P = lu_decomposition(A)

    # Permute b based on P
    Pb = np.dot(P, b)

    # Solve Ly = Pb for y (forward substitution)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (Pb[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Solve Ux = y for x (backward substitution)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x