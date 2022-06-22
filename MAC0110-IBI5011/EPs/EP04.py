n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

# Método iterativo para encontrar a quantidade de dígitos de 'n'
temp = n
cont = 0
while temp != 0:
    temp = temp // 10
    cont += 1

print(f'Quantidade de algarismos: {cont}')

# Calcula dv1 e dv2
temp = cont
s_1 = s_2 = 0
while temp > 0:
    alg = n % 10

    s_1 += temp * alg
    s_2 += (temp - 1) * alg

    print(f'{temp} x {alg}', end=' + ' if temp != 1 else ' ')

    n = n // 10
    temp -= 1

print(f'= {s_1}')

dv1 = s_1 % 11
print(f'{s_1} % {11} = {dv1}')

s_2 += dv1 * cont
dv2 = s_2 % 11
print(f'dv2 = {dv2}')
