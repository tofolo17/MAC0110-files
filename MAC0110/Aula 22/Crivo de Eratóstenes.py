def main():
    n = int(input('n: '))
    while not n > 0:
        n = int(input('n: '))

    limite = int(n ** 0.5)
    values = [i for i in range(2, n + 1)]

    for i in range(2, limite + 1):
        if primo(i):
            j = 0
            while j < len(values):
                if values[j] % i == 0 and values[j] != i:
                    values[j] = -1
                j += 1

    primos = [i for i in values if i != -1]
    print(primos)


def primo(n):
    if n != 2 and n % 2 == 0:
        return False
    else:
        i = 3
        while i < n // 2:
            if i % n == 0:
                return False
            i += 2
        return True


main()
