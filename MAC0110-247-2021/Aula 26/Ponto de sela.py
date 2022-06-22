def main():
    m = [
        [9, 8, 7],
        [5, 3, 2],
        [6, 6, 7]
    ]

    print(sela(m))


def retorna_coluna(matriz, index):
    coluna = []
    for linha in matriz:
        coluna += [linha[index]]

    return coluna


def sela(matriz):
    pontos = []
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            coluna = retorna_coluna(matriz, j)
            if max(linha) == min(coluna):
                pontos.append([i, j])

    return pontos


main()
