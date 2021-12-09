def main():
    notas = leia_notas()
    media = media_notas(notas)
    maiores = maiores_notas(notas, media)

    print(f'Valores digitados: {notas}')
    print(f'A média das notas é: {media}')
    print(f'Os seguintes valores estão acima da média: {maiores}')


def leia_notas():
    n = int(input('Número de notas: '))
    while not n > 0:
        n = int(input('Número de notas: '))

    i = 0
    values = []
    while i < n:
        v = float(input(f'{i + 1}ª nota: '))
        while not 0 <= v <= 10:
            v = float(input(f'{i + 1}ª nota: '))

        values += [v]

        i += 1

    return values


def media_notas(notas):
    return sum(notas) / len(notas)


def maiores_notas(notas, valor):
    maiores = []
    for nota in notas:
        if nota > valor:
            maiores += [nota]

    return maiores


main()
