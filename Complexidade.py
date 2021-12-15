def main():
    x = 5
    n = 5

    # sg(x, n)
    sg2(x, n)


def sg(x, n):
    """
    1 + x ** 1 + x ** 2 + ... x ** n
    """
    s = 0
    i = 0

    while i <= n:
        p = 1
        j = 0
        while j < i:
            p = p * x
            j += 1
        s = s + p
        i += 1

    print(s)


def sg2(x, n):
    s1 = 0
    s2 = 0

    contador = 0
    while contador < n:
        s1 = s1 + x ** contador
        s2 = s2 * x + 1

        print(s1 == s2)

        contador += 1


main()
