# Dado um número inteiro positivo, imprima sua representação binária.
n = int(input())

d = ""
while n > 0:
    r = n % 2
    if r == 1:
        d = "1" + d
    else:
        d = "0" + d
    n = n // 2

print(d)
