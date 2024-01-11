def jacobi(A: list, b: list, x0: list, e=10**-4):
    import numpy as np
    A = np.array(A)
    b = np.array(b)
    x0 = np.array(x0)
    n = len(A)

    Q = np.zeros([n, n])
    P = np.zeros([n, n])
    for i in range(n):
        Q[i][i] = 1/A[i][i]
        for j in range(n):
            if i != j:
                P[i][j] = -A[i][j]
    MJ = np.matmul(Q, P)
    if MJ < 1:
        x_norm = 1
        i = 0
        while x_norm > e:
            x = np.matmul(Q, np.matmul(P, x0) + b)
            x_norm = max(x-x0)
            x0 = x
            i += 1
        ans = x
        return Q, P, MJ, i, ans.round(3)
    else:
        return -1
