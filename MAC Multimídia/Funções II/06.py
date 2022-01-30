def main():
    n = int(input('n: '))
    while not n > 2:
        n = int(input('n: '))

    fn2, gn2 = valor(n - 2)
    print(fn2, gn2)

    fn200, gn200 = valor(n + 200)
    print(fn200, gn200)

    print(fn2 + gn200, fn200 - gn2)


def F(i):
    F1 = 2
    Fa = 1
    n = 3
    while n <= i:
        Fp = 2 * Fa + G(n - 2)
        Fa = Fp
        n += 1

    return Fa if i > 1 else F1


def G(i):
    G1 = 1
    Ga = 2
    n = 3
    while n <= i:
        Gp = Ga + 3 * F(n - 2)
        Ga = Gp
        n += 1

    return Ga if i > 1 else G1


def valor(k):
    return F(k), G(k)


main()
