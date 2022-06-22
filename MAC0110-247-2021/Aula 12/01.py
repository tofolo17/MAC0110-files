# Dado um número positivo N, determine se ele é primo.
n = int(input())

if n != 2 and n % 2 == 0:
    eh_primo = False
else:
    i = 3
    eh_primo = True  # indicador de passagem
    while i < n // 2 and eh_primo:
        if n % i == 0:
            eh_primo = False
        i += 2

print(eh_primo)
