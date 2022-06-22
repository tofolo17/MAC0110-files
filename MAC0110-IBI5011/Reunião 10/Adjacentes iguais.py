n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

alg = n % 10
i = n // 10

adjacentes = False
while i > 0 and not adjacentes:
    temp_alg = alg
    alg = i % 10
    i = i // 10

    if temp_alg == alg:
        adjacentes = True

print(adjacentes)
