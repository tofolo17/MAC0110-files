def main():
    m, n = 2, 3  # atribuição múltipla
    x = f(m, n)
    print(f"m={m} n={n} x={x}")


def f(n, m):
    x = m + n
    m, n = n, m  # troca m e n
    return -1


main()
