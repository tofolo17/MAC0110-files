def main():
    print(soma_frac(1, 2, 3, 4))


def soma_frac(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2

    _mdc = mdc(n, d)

    return n // _mdc, d // _mdc  # Retorna dois inteiros


def mdc(a, b):
    d = min(a, b)
    while not (a % d == 0 and b % d == 0):
        d -= 1

    return d


main()
