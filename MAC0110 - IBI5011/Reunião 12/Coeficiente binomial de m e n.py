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


n1 = int(input('n: '))
m1 = int(input('m: '))

print(binomial(m1, n1))
