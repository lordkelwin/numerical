def gaussianelim(A: list[float], b: list[float]):
    n = len(A)
    for i in range(n):
        A[i] += b[i]
    # Forward elimination
    for i in range(n):
        for j in range(i+1, n):
            if A[j][i] != 0:
                ratio = A[i][i] / A[j][i]  # obtaining the factor
                for k in range(i, n+1):
                    A[j][k] = A[i][k] - (ratio * A[j][k])
    # Reverse elimination
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n + 1):
                A[j][k] -= (ratio * A[i][k])
    # Checking if the diagonal elements is zero
    for i in range(n):
        if A[i][i] == 0:
            return -1  # return -1 because it has no solution
    # Getting the solution
    sol = {}
    for i in range(n):
        A[i][n] /= A[i][i]
        A[i][i] /= A[i][i]
        sol[f'x{i+1}'] = round(A[i][n], 6)

    return sol
