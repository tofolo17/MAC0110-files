nota = int(input('Nota: '))

if nota > 8:
    msg = "+++"
elif nota >= 5:
    msg = "APR"
else:
    msg = "REC"

print(f"NOTA --> {msg}")
