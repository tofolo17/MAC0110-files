def main():
    print('Preencha o gabarito:')
    gabarito = popula_prova()

    n = int(input('Número de estudantes: '))
    for i in range(1, n + 1):
        print(f'Preencha a prova do aluno {i}: ')
        prova = popula_prova()
        acertos = calcula_acertos(gabarito, prova)
        print(f'Acertos: {acertos}')


def popula_prova():
    prova = []
    for i in range(1, 31):
        q = input(f'Alternativa da {i}° questão: ')
        while not (q in ['ABCDE']):
            q = input(f'ERRO. Alternativa da {i}° questão: ')
        prova += [q]

    return prova


def calcula_acertos(gabarito, prova):
    acertos = 0
    for i in range(30):
        if gabarito[i] == prova[i]:
            acertos += 1

    return acertos


main()
