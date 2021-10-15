n = int(input("Digite o valor a ser retirado: "))

print(f'O seu valor de: R$ {format(n, ".2f")} reais corresponde a:')

notas_200 = n // 200
resto = n % 200
print(f'{notas_200} nota(s) de R$ 200,00')

notas_100 = resto // 100
resto = resto % 100
print(f'{notas_100} nota(s) de R$ 100,00')

notas_50 = resto // 50
resto = resto % 50
print(f'{notas_50} nota(s) de R$ 50,00')

notas_20 = resto // 20
resto = resto % 20
print(f'{notas_20} nota(s) de R$ 20,00')

notas_10 = resto // 10
resto = resto % 10
print(f'{notas_10} nota(s) de R$ 10,00')

notas_5 = resto // 5
resto = resto % 5
print(f'{notas_5} nota(s) de R$ 5,00')

notas_2 = resto // 2
resto = resto % 2
print(f'{notas_2} nota(s) de R$ 2,00')

moedas_1 = resto
print(f'{moedas_1} moeda(s) de R$ 1,00')
