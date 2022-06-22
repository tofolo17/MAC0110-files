n = int(input(f"n: "))
while not n > 0:
    n = int(input(f"n: "))

i = 0
pares = impares = 0
while i < n:
    m = int(input(f'{i + 1}° número: '))

    if m % 2 == 0:
        pares += 1
    else:
        impares += 1

    i += 1

print(f'Pares: {pares}\nÍmpares: {impares}')
