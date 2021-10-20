n = int(input())

d = 2
i = n
while i > 1:

    cont = 0
    while i % d == 0:
        cont += 1
        i = i / d

    if cont != 0:
        print(d, cont)

    d += 1
