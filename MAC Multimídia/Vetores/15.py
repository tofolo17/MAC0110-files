def main():
    n = int(input('n > 0: '))
    k = int(input('k > 0: '))

    pesos = populate(k)

    somas = [0] * k
    for i in range(n):
        mp = 0
        print(f'\nAluno {i + 1}.')
        for j in range(k):
            nota = float(input(f'Nota na prova {j + 1} (0 <= nota <= 10): '))
            mp += pesos[j] * nota
            somas[j] += nota
        print(f'Média ponderada: {mp / sum(pesos)}')

    for i in range(len(somas)):
        print(f'Média aritmética na prova {i + 1}: {somas[i] / n}')


def populate(n):
    lista = []
    for i in range(n):
        v = int(input(f'Peso da {i + 1}ª prova: '))
        lista += [v]

    return lista


main()
