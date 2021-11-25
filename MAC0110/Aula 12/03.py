"""
Dado um número inteiro positivo n maior que 1 e um dígito d,
compute o número obtido removendo a primeira ocorrência do dígito d > 0 em n.
"""
n = int(input())
d = int(input())

inv_n = 0
while n > 0:
    alg = n % 10
    inv_n = inv_n * 10 + alg
    n = n // 10

r = 0
retirado = False
while inv_n > 0:
    alg = inv_n % 10
    if alg != d or retirado:
        r = r * 10 + alg
    elif alg == d:
        retirado = True
    inv_n = inv_n // 10

print(r)
