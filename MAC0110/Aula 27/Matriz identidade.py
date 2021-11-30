def main():
    n = 10
    m = matriz_identidade(n)

    print(m)


def matriz_identidade(n):
    m = cria_matriz(n, n)

    j = 0
    for i in range(len(m)):
        linha = list(m[i])
        linha[j] = 1
        m[i] = linha

        j += 1

    return m


def cria_matriz(linhas, colunas, v=0):
    linha_0 = [v for _ in range(colunas)]
    return repete(linha_0, linhas)


def repete(values, linhas):
    return [values for _ in range(linhas)]


main()
