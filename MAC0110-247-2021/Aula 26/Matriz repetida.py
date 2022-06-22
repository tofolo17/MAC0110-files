"""n = int(input('Quantidade de valores na lista: '))
while not n > 0:
    n = int(input('Quantidade de valores na lista: '))

values = []
for i in range(n):
    v = int(input(f'{i + 1}° valor: '))
    values += [v]

m = int(input(f'Quantidade de linhas da matriz m-por-n: '))
while not m > 0:
    m = int(input(f'Quantidade de linhas da matriz m-por-n: '))"""

values = [1, 2, -6]
m = 4

m = [values for i in range(m)]

print(m)
print(m[2][0])
