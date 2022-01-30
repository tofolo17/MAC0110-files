def main():
    print('n pontos e seus raios de uma circunferência com centro no ponto P(x, y)')

    print('Ponto P:')
    x = float(input('x: '))
    y = float(input('y: '))

    n = int(input('\nQuantidade de pontos: '))
    while not (0 <= n <= 100):
        n = int(input('\nQuantidade de pontos: '))

    rs = []
    for i in range(1, n + 1):
        print(f'\nPonto N{i}')
        xi = float(input('x: '))
        yi = float(input('y: '))

        r = ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5
        if r not in rs:
            rs += [r]

    print(f'Raios sem repetição: {rs}')


main()
