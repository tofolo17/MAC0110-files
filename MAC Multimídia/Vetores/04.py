def main():
    print('Produto escalar entre vetores x e y')
    n = int(input('Número de elementos dos vetores: '))

    print('\nVetor x:')
    x = popula_vetor(n)

    print(f'\nVetor y:')
    y = popula_vetor(n)

    p = prod_escalar(x, y, n)
    print(f'O produto escalar entre x e y vale: {p}')


def popula_vetor(n):
    vetor = []
    for i in range(1, n + 1):
        v = float(input(f'{i}° componente: '))
        vetor += [v]

    return vetor


def prod_escalar(x, y, n):
    p = []
    for i in range(n):
        p += [x[i] * y[i]]

    return p


main()
