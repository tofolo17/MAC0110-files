def main():
    n = int(input())
    while not n > 0:
        n = int(input())

    print(hde(n))


def hde(n):
    return hdir(n), hesq(n)


def hdir(n):  # Maior até o menor
    s, i = 0, 1
    while i <= n:
        s += 1 / i
        i += 1

    return s


def hesq(n):  # Menor até o maior --> Mais preciso! Para melhorar, podemos somar frações!
    s, i = 0, n
    while i > 0:
        s += 1 / i
        i -= 1

    return s


if __name__ == '__main__':  # Não sei quando devo usar isso...
    main()
