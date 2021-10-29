def main():
    print(h(3))


def h(n):
    return hf_dir(n), hf_esq(n)


def hf_dir(n):
    i = 2
    sn, sd = 1, 1
    while i <= n:
        sn, sd = soma_frac(sn, sd, 1, i)
        i += 1

    return sn / sd


def hf_esq(n):
    sn, sd = 1, n
    while n > 1:
        sn, sd = soma_frac(sn, sd, 1, n - 1)
        n -= 1

    return sn / sd


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
