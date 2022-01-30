def main():
    print('Frequência na sequência de n elementos')
    n = int(input('n: '))

    seq = []
    freq = {}
    for i in range(1, n + 1):
        v = float(input(f'{i}° elemento: '))
        seq += [v]
        if v not in freq:
            freq[v] = 1
        else:
            freq[v] += 1

    print(f'Sequência: {seq}')
    for chave, valor in freq.items():
        print(f'{chave} aparece {valor} vezes')


main()
