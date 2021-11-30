def main():
    m = 3
    n = 5

    matrix = cria_matriz(m, n)

    cont = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = cont
            cont += 1

    print(matrix)


def cria_matriz(m, n):
    return repete([0 for _ in range(n)], m)


def repete(values, m):
    return [values for _ in range(m)]


main()
