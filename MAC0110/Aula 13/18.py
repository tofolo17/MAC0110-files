def eh_primo(n):  # baseado no exercício 01, versão 02 do professor, aula 12.

    if n != 2 and n % 2 == 0:  # Se não for o 2 e for divisível por 2
        primo = False

    else:  # Números ímpares não são divisíveis por números pares. Logo, i += 2.
        i = 3
        primo = True
        while i < n // 2 and primo:
            if n % i == 0:
                primo = False
            i += 2

    return primo


num = int(input("N: "))
while not num > 0:
    num = int(input("N: "))

cont = num
while cont > 0:
    if eh_primo(cont) and eh_primo(num - cont):
        print(cont, num - cont)
    cont -= 1

print("Acabou.")
