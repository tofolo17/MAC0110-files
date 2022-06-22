def main():
    matriz = [
        [0, 0, 0],
        [1, 1, 1]
    ]

    print(conta_linhas(matriz))
    print(conta_colunas(matriz))


def conta_linhas(matriz):
    return len(matriz)


def conta_colunas(matriz):
    return len(matriz[0])


main()
