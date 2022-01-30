def main():
    print('Soma de dois inteiros representados por sequências a e b de tamanho n')
    n = int(input('n > 0: '))

    print(f'\na: ')
    a = popula_numero(n)

    print(f'\nb: ')
    b = popula_numero(n)

    s = soma(a, b, n)
    print(s)


def popula_numero(n):
    num = [0]
    for i in range(1, n + 1):
        alg = int(input(f'{n + 1 - i}° algarismo: '))
        num += [alg]

    return num


def soma(a, b, n):
    ac = [0] * (n + 1)
    r = []

    for i in range(n - 1, -1, -1):
        s = a[i] + b[i] + ac[i + 1]
        print(s)

        if s >= 10:
            r = [s % 10] + r
            ac[i] = 1
        else:
            r = [s] + r

        print(r, ac, '\n')

    return [ac[0]] + r


main()
