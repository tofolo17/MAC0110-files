soma = 0
num = int(input())

while num >= 0:
    if num % 2 == 0:
        soma += num
    num = int(input())

print(soma)
