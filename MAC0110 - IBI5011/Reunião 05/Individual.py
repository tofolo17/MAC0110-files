nota = int(input('Nota: '))

if nota > 8:
    msg = "+++"
elif nota >= 5:
    msg = "APR"
elif nota >= 3:
    msg = "REC"
else:
    msg = "REC"

print(f"NOTA --> {msg}")
