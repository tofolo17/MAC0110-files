def main():
    """print('Multiplicação de matrizes A e B\n')
    print('Matriz A')
    mA = int(input('Número de linhas da matriz A: '))
    nA = int(input('Número de colunas da Matriz A: '))"""
    A = [[2, 3], [-4, 0]]  # le_matriz(mA, nA)

    """print('\nMatriz B')
    print(f'Número de linhas da matriz B: {nA}')
    nB = int(input('Número de colunas da matriz B: '))"""
    B = [[7, 2], [-1, 2]]  # le_matriz(nA, nB)

    print('\nMultiplicação')
    M = multiplica(A, B)
    print(M)


def le_matriz(m, n):
    C = []
    for i in range(m):
        L = []
        for j in range(n):
            v = float(input(f'{i + 1}{j + 1}: '))
            L += [v]
        C.append(L)

    return C


def multiplica(A, B):
    C = []
    for i in range(len(A)):
        L = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            L += [s]
        C.append(L)

    return C


main()
