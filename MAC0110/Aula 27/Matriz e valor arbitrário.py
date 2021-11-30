def main():
    li = 3
    c = 5
    v = 2

    m = matriz_cheia(li, c, v)

    print(m)


def matriz_cheia(linhas, colunas, valor_arbitrario):
    return cria_matriz(linhas, colunas, valor_arbitrario)


def cria_matriz(linhas, colunas, v=0):
    linha_0 = [v for _ in range(colunas)]
    return repete(linha_0, linhas)


def repete(values, linhas):
    return [values for _ in range(linhas)]


main()
