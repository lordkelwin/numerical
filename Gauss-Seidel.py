def GaussSeidel(A: list[float], b: list[float], x0: list[float], e=10**-4):
    import numpy as np
    n = len(A)
    D = np.zeros([n, n])
    L = np.zeros([n, n])
    U = np.zeros([n, n])

    for i in range(n):
        D[i][i] = A[i][i]
        for j in range(n):
            if i != j:
                if i > j:
                    L[i][j] = A[i][j]
                elif i < j:
                    U[i][j] = A[i][j]

    DL = np.linalg.inv(D+L)
    M_gs = np.matmul(DL, -U)
    U = -U
    # if M_gs.max() < 1:
    x_norm = 1
    i = 0
    while x_norm > e:
        x = np.matmul(DL, np.matmul(U, x0)+b)
        x_norm = max(abs(x-x0))
        x0 = x
        i += 1
    return DL, U, M_gs.max(), x_norm, i, x.round(3)
    # else:
    #    return -1
