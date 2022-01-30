def main():
    print('Coeficientes reais da primeira derivada de p(x)')
    n = 5

    coefs = popula_polinomio(n)

    der = []
    for i in range(1, n):
        coef_der = coefs[n - 1 - i] * i
        der += [coef_der]

    print(der)


def popula_polinomio(n):
    pol = []
    for i in range(n):
        coef = float(input(f'a{i}: '))
        pol = [coef] + pol

    return pol


main()
