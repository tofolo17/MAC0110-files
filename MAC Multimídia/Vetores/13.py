def main():
    px = [0, 2, 1, 1]  # polinomio()
    qx = [2, 3, -4, 2]  # polinomio()

    prod = prod_polinomio(px, qx)
    print(prod)


def polinomio():
    n = int(input('n: '))

    coefs = []
    for i in range(n):
        coef = float(input(f'a{i}: '))
        coefs = coefs + [coef]

    return coefs


def prod_polinomio(px, qx):
    a = len(px)
    b = len(qx)
    p = [0] * (a + b - 1)
    print(p)
    for i in range(a):
        for j in range(b):
            p[i + j] += px[i] * qx[j]
    return p


main()
