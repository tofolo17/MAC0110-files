# Problema: Dado um inteiro N > 0, listar todos os primos menores ou iguais a N

def eh_primo(n):  # baseado no exercício 01, versão 01 do professor, aula 12.
    i = 2
    primo = True
    while n > i and primo:
        if n % i == 0:
            primo = False
        i += 1

    return primo


num = int(input("N: "))
while not num > 0:
    num = int(input("N: "))

cont = num
while cont > 1:
    if eh_primo(cont):
        print(cont, end=" ")
    cont -= 1
