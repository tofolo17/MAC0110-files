def main():
    print('Sequência de n números e sua inversa')
    n = int(input('n > 0: '))

    inversa = popula_inversa(n)
    print(f'A sequência inversa é: {inversa}')


def popula_inversa(n):
    inversa = []
    for i in range(1, n + 1):
        v = float(input(f'{i}° termo: '))
        inversa = [v] + inversa

    return inversa


main()
