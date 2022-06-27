def main():
    print('Lê e imprime Matriz A m-por-n')
    m = int(input('m: '))
    n = int(input('n: '))
    A = le_matriz(m, n)

    imprime_matriz(A)


# a)
def le_matriz(m, n):
    A = []
    for i in range(m):
        print(f'Linha {i + 1}')
        L = []
        for j in range(n):
            t = float(input(f'{j + 1}° termo: '))
            L += [t]
        A.append(L)

    return A


# b)
def imprime_matriz(A):
    for linha in A:
        print(linha)


main()
