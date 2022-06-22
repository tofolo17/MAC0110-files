def main():
    lst = [1, 3, 8, -3]  # leia_seq()

    ini, fim, soma = fatia_max(lst)
    print(ini, fim, soma)


def leia_seq():
    n = int(input('Número de elementos: '))
    while not n > 0:
        n = int(input('Número de elementos: '))

    i = 0
    seq = []
    while i < n:
        v = int(input(f'{i + 1}º valor: '))
        seq += [v]

        i += 1

    return seq


def fatia_max(lst):
    m = 0
    imax = 0
    jmax = 0

    n = len(lst)
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            print(lst, lst[i:j])
            s = sum(lst[i:j])
            if s > m:
                m = s
                imax = i
                jmax = j

    return imax, jmax, m


main()
