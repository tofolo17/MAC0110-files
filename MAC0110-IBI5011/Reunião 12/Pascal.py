def main():
    m = int(input('m: '))

    i = 0
    while i <= m:
        print(binomial(m, i), end=" ")
        i += 1


def fatorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1

    return r


def binomial(m, n):
    numerador = fatorial(m)
    denominador = fatorial(n) * fatorial(m - n)

    return numerador / denominador


if __name__ == '__main__':
    main()
