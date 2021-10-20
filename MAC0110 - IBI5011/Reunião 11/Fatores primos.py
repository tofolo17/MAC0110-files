"""
Decomposição em fatores primos talvez não precise verificar se é primo ou não, e só ir somando += 1 no divisor
"""


def eh_primo(num):
    j = 2

    primo = True
    while j < num and primo:
        if num % j == 0:
            primo = False
        j += 1

    return primo


n = int(input())

d = 2
cont = 0

i = n
while i > 1:

    # Se for divisível, aumenta a multiplicidade do divisor primo 'd'
    if i % d == 0:
        cont += 1
        i = i / d

        if i == 1:
            print(d, cont)

    # Se não, procuramos um novo 'd'
    else:
        if cont != 0:
            print(d, cont)

        d += 1
        cont = 0
        while not eh_primo(d):
            d += 1
