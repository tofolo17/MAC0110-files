def main():
    a = [1, 2, 3, 4, 5]
    copia_errada(a)

    a = [1, 2, 3, 4, 5]
    copia_correta(a)


def copia_errada(a):
    b = a
    b[1] = 7
    print(f'{a}\n{b}\n')


def copia_correta(a):
    # b = list(a)
    # b = a[0:len(a)] ou a[:]
    b = a.copy()
    b[1] = 7
    print(f'{a}\n{b}\n')


main()
