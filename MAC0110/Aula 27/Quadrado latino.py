def main():
    A = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]
    ]

    print(quadrado_latino(A))


def retorna_coluna(indice, matriz):
    return [linha[indice] for linha in matriz]


def quadrado_latino(matriz):
    n = len(matriz)

    for i in range(n):
        linha = matriz[i]
        coluna = retorna_coluna(i, matriz)

        for j in range(1, n + 1):
            if not (j in linha or j in coluna):
                return False

    return True


main()
