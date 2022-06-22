# Dado um número inteiro, imprima o número ao contrário.
D = int(input())
Dstat = D
DC = 0

while D > 0:
    d = D % 10
    print(f"Digito atual: {d}")
    DC = DC * 10 + d
    print(f"Número ao contrário atual: {DC}")
    D = D // 10

print(Dstat, DC)
if Dstat == DC:
    print("Palíndromo")
