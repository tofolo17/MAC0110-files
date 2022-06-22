def main():
    A = [
        [1, 2, 3, 5],
        [2, 1, 2, 4],
        [3, 2, 1, 1],
        [3, 2, 1, 1]
    ]

    print(preenche_borda(A))


def preenche_borda(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    linha_zerada = [0 for _ in range(colunas)]

    matriz[0] = linha_zerada
    matriz[-1] = linha_zerada

    for i in range(1, linhas - 1):
        for j in [0, colunas - 1]:
            matriz[i][j] = 0

    return matriz


main()
