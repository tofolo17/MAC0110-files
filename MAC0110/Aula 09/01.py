# Dado um número inteiro, imprima os digitos deste número.
D = int(input())

while D > 0:
    d = D % 10
    print(f"Digito atual: {d}")
    D = D // 10
    print(f"O número atual: {D}")
