def main():
    m = 5  # int(input('m: '))
    n = 8  # int(input('n: '))

    # le_matriz(m, n)
    A = [
        [0, -1, 0, -1, -1, 0, -1, 0],
        [0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, -1, 0],
        [-1, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, -1, 0, 0, 0, -1, -1]
    ]

    Am = moldura(A, m, n)

    cont = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(i, j)
            if inicio(Am, i, j):
                cont += 1
                Am[i][j] = cont

    for i in range(1, m + 1):
        print()
        for j in range(1, n + 1):
            print(Am[i][j], end=' ')


def le_matriz(m, n):
    A = []
    for i in range(m):
        L = []
        for j in range(n):
            v = int(input(f'A{i + 1}{j + 1} [0/-1]: '))
            L += [v]
        A.append(L)

    return A


def moldura(A, m, n):
    ms = [-1] * (n + 2)
    M = [ms]

    for linha in A:
        M.append([-1] + linha + [-1])
    M.append(ms)

    return M


def inicio(A, i, j):
    return A[i][j] != -1 and ((A[i - 1][j] == -1 and A[i + 1][j] != -1) or (A[i][j - 1] == -1 and A[i][j + 1] != -1))


main()
