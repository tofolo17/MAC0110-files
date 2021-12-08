s = input('Seu texto: ')

cont = 0
for char in s:
    if char in 'aeiou':
        cont += 1

print(cont / len(s))
