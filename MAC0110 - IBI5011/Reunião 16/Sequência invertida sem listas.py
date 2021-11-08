def main():
    n = int(input('Quantidade de números: '))

    i = 0
    ns = 0
    ns_digits = 0
    while i < n:
        v = int(input(f'{i + 1}°: '))
        v_digits = digitos(v)

        ns_digits = ns_digits * 10  # Encontrado possível impasse
        ns = ns * 10 ** v_digits + v

        i += 1

    print(ns)


def digitos(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1

    return i


main()
