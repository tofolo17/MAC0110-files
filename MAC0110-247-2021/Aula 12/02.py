"""
Dados um número inteiro positivo n maior que 2, e uma sequência de n números inteiros positivos,
verifique se a sequência é uma progressão aritmética.
"""
n = int(input("Quantidade de termos: "))

n1 = int(input())
n2 = int(input())

k1 = n2 - n1

i = 0
eh_sequencia = True
while i < n - 2:
    n1 = n2
    n2 = int(input())

    k2 = n2 - n1

    if k1 != k2:
        eh_sequencia = False

    i += 1

print(eh_sequencia)
