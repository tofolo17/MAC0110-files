n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

i = 0
values = []
while i < n:
    v = int(input(f'{i + 1}°: '))
    if v not in values:
        values += [v]
    i += 1

print(values)
