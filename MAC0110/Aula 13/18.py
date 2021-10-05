def eh_primo(n):  # baseado no exercício 01, versão 02 do professor, aula 12.
    if n != 2 and n % 2 == 0:
        primo = False
    else:
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

"""
pode_ser_escrito = False
cont = num
while cont > 1:  # Devo incluir o 1 como primo?
    if eh_primo(cont):
        cont2 = cont
        while cont2 > 1:
            if eh_primo(cont2):
                if cont + cont2 == num:
                    print(f'{cont} + {cont2} = {num}')
                    pode_ser_escrito = True
            cont2 -= 1
    cont -= 1
"""

print("Acabou.")
