def main():
    print('Linhas e colunas nulas da matriz A\n')

    m = 4  # int(input('Número de linhas de A: '))
    n = 4  # int(input('Número de colunas de A: '))
    A = [[1, 0, 2, 3], [4, 0, 5, 6], [0, 0, 0, 0], [0, 0, 0, 0]]  # le_matriz(m, n)

    nulos = conta_nulos(A, m, n)
    print(nulos)


def le_matriz(m, n):
    A = []
    for i in range(m):
        L = []
        for j in range(n):
            v = int(input(f'A{i + 1}{j + 1}: '))
            L += [v]
        A.append(L)

    return A


def conta_nulos(A, m, n):
    l = 0
    c = 0

    L_0 = [0] * n
    C_0 = [0] * m

    for i in range(m):
        L = A[i]
        if L == L_0:
            l += 1

        C = []
        for j in range(n):
            C += [A[j][i]]
        if C == C_0:
            c += 1

    return l, c


main()
