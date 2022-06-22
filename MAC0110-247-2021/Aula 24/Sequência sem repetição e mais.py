def main():
    n = int(input('n: '))
    while not n > 0:
        n = int(input('n: '))

    i = 0
    values = []
    while i < n:
        v = int(input(f'{i + 1}°: '))
        values += [v]
        i += 1

    print(values)

    set_values = unicos(values)
    print(set_values)


def pertence(n, values):
    for value in values:
        if value == n:
            return True
    return False


def unicos(values):  # Bem inútil no contexto do programa
    set_values = []
    for value in values:
        if not pertence(value, set_values):
            set_values += [value]

    return set_values


def posicao(n, values):
    i = 0
    while i < n:
        if n == values[i]:
            return i
        i += 1

    return -1


def insira_novo(n, values):
    p = posicao(n, values)
    if p == -1:
        values += [n]
        p = len(values) - 1
    return p


main()
