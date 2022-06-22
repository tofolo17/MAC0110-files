n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

i = 1
crescente = True
m = int(input('1° número: '))
while i < n and crescente:
    temp = m
    m = int(input(f'{i + 1}° número: '))
    if temp >= m:
        crescente = False
    i += 1

print(crescente)
