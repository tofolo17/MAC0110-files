def main():
    n = int(input('n: '))
    while not n > 0:
        n = int(input('n: '))

    limite = int(n ** 0.5)
    values = [i for i in range(2, n + 1)]

    for i in range(2, limite + 1):
        for j in range(len(values)):
            if values[j] % i == 0 and values[j] != i:
                values[j] = -1

    primos = [i for i in values if i != -1]
    print(primos)


main()
