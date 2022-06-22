def main():
    n = int(input('n: '))
    while not n > 1:
        n = int(input('n: '))

    print(fat(n))


def fatorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1

    return r


def fat(n):
    return fatorial(n) / 2


if __name__ == '__main__':
    main()
