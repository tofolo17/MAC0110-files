s = "Eu adoro bola de sabão malucamaluca"
s = s + " "  # Evita tratamento especial da última palavra

i = 0
m = 0
cont = 0

while i < len(s):
    char = s[i]

    if char != " ":
        cont += 1
    else:
        if cont > m:
            m = cont
        cont = 0

    i += 1

print(m)
