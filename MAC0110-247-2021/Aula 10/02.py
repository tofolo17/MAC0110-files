# Dada uma sequência de números positivos quaisquer terminada em zero, determine se a sequência está em ordem crescente.
n_1 = int(input())
n_2 = int(input())

crescente = True
while n_2 != 0:
    if n_1 > n_2:
        crescente = False
    n_1 = n_2
    n_2 = int(input())

print(crescente)
