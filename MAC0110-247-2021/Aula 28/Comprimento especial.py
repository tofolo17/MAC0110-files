s = "Olá! Me chamo Gustavo, e você?"
s = s + " "

special_chars = " !.,;?[]():'\""

m = 0
cont = 0
for char in s:
    if char not in special_chars:
        cont += 1
    else:
        if cont > m:
            m = cont
        cont = 0

print(m)
