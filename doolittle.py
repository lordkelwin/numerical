def doolittle(A: list[float], b: list[float]):
    import LU_decomposition
    n = len(A)
    L, U = LU_decomposition.LU(A)

    L = L.tolist()
    for i in range(n):
        L[i] += b[i]

    for i in range(n):
        for j in range(i + 1, n):
            if L[j][i] != 0:
                ratio = L[i][i] / L[j][i]  # obtaining the factor
                for k in range(i, n+1):
                    L[j][k] = L[i][k] - (ratio * L[j][k])

    for i in range(n):
        L[i][n] /= L[i][i]
        L[i][i] /= L[i][i]

    U = U.tolist()
    for i in range(n):
        U[i].append(L[i][n])

    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            ratio = U[j][i] / U[i][i]
            for k in range(i, n + 1):
                U[j][k] -= (ratio * U[i][k])

    for i in range(n):
        if U[i][i] == 0:
            return -1  # return -1 because it has no solution
    # Getting the solution
    sol = {}
    for i in range(n):
        U[i][n] /= U[i][i]
        U[i][i] /= U[i][i]
        sol[f'x{i+1}'] = round(U[i][n], 3)

    return sol