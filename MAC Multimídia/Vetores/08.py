def main():
    print('Lê duas listas ordenadas de tamanho n e m e retorna a junção destas, também ordenada.')

    # n = int(input('n: '))
    lista_1 = [1, 2, 7, 8, 13, 14]  # popula_ordenada(n)

    # m = int(input('\nm: '))
    lista_2 = [1, 2, 2, 2, 2, 5, 66]  # popula_ordenada(m)

    r = junta_e_ordena(lista_1, lista_2)
    print(r)


def popula_ordenada(tamanho):
    lista = []
    a = float(input('1° elemento: '))
    for i in range(2, tamanho + 1):
        p = float(input(f'{i}° elemento: '))
        while not (p >= a):
            p = float(input(f'ERRO. {i}° elemento: '))

        lista += [p]
        a = p

    return lista


def junta_e_ordena(lista_1, lista_2):
    r = []
    i, j = 0, 0
    while i < len(lista_1) and j < len(lista_2):
        if lista_1[i] > lista_2[j]:
            r += [lista_2[j]]
            j += 1
        else:
            r += [lista_1[i]]
            i += 1

    if j == len(lista_2):
        r += lista_1[i:len(lista_1)]
    if i == len(lista_1):
        r += lista_2[j:len(lista_2)]

    return r


main()
