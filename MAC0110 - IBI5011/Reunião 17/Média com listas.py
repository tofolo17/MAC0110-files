def main():
    n = int(input('Digite o número de notas: '))
    while not n > 0:
        n = int(input('Digite o número de notas: '))

    notas = []
    for i in range(n):
        v = float(input(f'Digite a {i + 1}ª nota: '))
        while not 0 <= v <= 10:
            v = float(input(f'Valor inválido. Digite a {i + 1}ª nota: '))

        notas += [v]

    media = sum(notas) / n
    print(f'A média das notas é: {media}')

    maiores = 0
    for nota in notas:
        if nota > media:
            maiores += 1

    print(f'{maiores} nota(s) maiores que {media}')


main()
