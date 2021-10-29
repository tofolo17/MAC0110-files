def main():
    print(soma_frac(1, 2, 3, 4))


def soma_frac(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2

    # Implementar MDC para não ter que fatorar

    return n, d


def mdc():
    pass


main()
