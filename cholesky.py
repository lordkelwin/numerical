def choleskyFactor(A: list[float]):
    import numpy as np
    import math
    A = np.array(A)
    assert A[0][0] > 0, 'The matrix is not positive definitive.'
    assert np.linalg.det(A) > 0, 'The matrix is not positive definitive.'
    assert np.linalg.det(np.array([[A[0][0], A[0][1]], [A[1][0], A[1][1]]])) > 0, \
        'The matrix is not positive definitive.'
    n = len(A)
    L = np.zeros([n, n])
    for i in range(n):
        L[i][i] = math.sqrt(A[i][i] - sum(L[i][:i] ** 2))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][:i])*sum(L[i][:i]))/L[i][i]

    LT = L.transpose()

    return L, LT


def choleskyMethod(A: list[float], b: list[float]):
    n = len(A)
    L, LT = choleskyFactor(A)

    L = L.tolist()
    for i in range(n):
        L[i] += b[i]

    for i in range(n):
        for j in range(i + 1, n):
            if L[j][i] != 0:
                ratio = L[i][i] / L[j][i]  # obtaining the factor
                for k in range(i, n + 1):
                    L[j][k] = L[i][k] - (ratio * L[j][k])

    for i in range(n):
        L[i][n] /= L[i][i]
        L[i][i] /= L[i][i]

    LT = LT.tolist()
    for i in range(n):
        LT[i].append(L[i][n])

    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            ratio = LT[j][i] / LT[i][i]
            for k in range(i, n + 1):
                LT[j][k] -= (ratio * LT[i][k])

    for i in range(n):
        if LT[i][i] == 0:
            return -1  # return -1 because it has no solution
    # Getting the solution
    sol = {}
    for i in range(n):
        LT[i][n] /= LT[i][i]
        LT[i][i] /= LT[i][i]
        sol[f'x{i + 1}'] = round(LT[i][n], 3)

    return sol
