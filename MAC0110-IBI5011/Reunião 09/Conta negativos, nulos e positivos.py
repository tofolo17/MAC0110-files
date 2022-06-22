n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

i = 0
positivos = negativos = nulos = 0
while i < n:
    m = int(input(f'{i + 1}° número: '))

    if m > 0:
        positivos += 1
    elif m == 0:
        nulos += 1
    else:
        negativos += 1

    i += 1

print(f'Positivos: {positivos}\nNulos: {nulos}\nNegativos: {negativos}')
