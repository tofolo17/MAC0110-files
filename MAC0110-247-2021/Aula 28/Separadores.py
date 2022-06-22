s = "Olá, Guga. Tudo bem?"  # input('Texto: ')
seps = " ,."  # input('Separadores: ')

s += " "

inicio = fim = 0
while fim < len(s):
    char = s[fim]

    if char in seps:
        if fim - inicio > 0:
            print(f'{s[inicio: fim]}')
        inicio = fim + 1

    fim += 1
