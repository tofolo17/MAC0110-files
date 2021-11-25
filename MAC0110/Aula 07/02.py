soma = 0
num = int(input())

contador = 0
while num >= 0:
    contador += 1
    soma += num
    num = int(input())

print(soma, contador, soma / contador)
