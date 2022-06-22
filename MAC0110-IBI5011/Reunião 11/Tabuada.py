n = int(input('n: '))
m = int(input('m: '))

i = 1
while i <= n:
    print(f'Tabuada do {i}')

    j = 1
    while j <= m:
        print(f'{i} x {j} = {i * j}')
        j += 1

    i += 1
