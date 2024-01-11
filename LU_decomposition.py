def LU(A: list[float]):
    import numpy as np
    from copy import deepcopy
    n = len(A)
    U = deepcopy(A)
    L = np.identity(n)

    for i in range(n):
        for j in range(i+1, n):
            if U[j][i] != 0:
                ratio = U[j][i] / U[i][i]
                for k in range(i, n):
                    U[j][k] = U[j][k] - (ratio * U[i][k])
                L[j][i] = ratio

    U = np.array(U)
    return L, U
