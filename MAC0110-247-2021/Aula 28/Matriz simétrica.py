def main():
    A = [
        [1, 2, 3],
        [2, 1, 2],
        [3, 2, 1]
    ]

    print(matriz_simetrica(A))


def retorna_coluna(indice, matriz):
    return [linha[indice] for linha in matriz]


def matriz_simetrica(matriz):
    n = len(matriz)

    for i in range(n):
        linha = matriz[i]
        coluna = retorna_coluna(i, matriz)

        if not (linha == coluna):
            return False

    return True


main()
