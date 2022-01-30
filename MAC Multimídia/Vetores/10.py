def main():
    n = int(input('Quantidade de coeficientes: '))
    coefs = popula_lista(n)

    m = int(input('Quantidade de pontos: '))
    xs = popula_lista(m)

    pxs = []
    for x in xs:
        px = 0
        for i in range(n):
            px += coefs[i] * x ** i
        pxs += [px]

    print(pxs)


def popula_lista(n):
    lista = []
    for i in range(1, n + 1):
        v = float(input(f'{i}°: '))
        lista += [v]

    return lista


main()
