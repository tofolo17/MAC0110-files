import random


def main():
    print('Verificação de confiabilidade em dado a partir de n lançamentos')
    n = int(input('n: '))
    resultados = [0] * 6

    for i in range(n):
        r = random.randint(0, 5)
        resultados[r] += 1

    for i in range(len(resultados)):
        print(f'{i + 1}: {resultados[i]}')


main()
