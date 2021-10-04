notas = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
grau = str()

for nota in notas:
    if nota >= 90:
        grau = "A"
    elif nota >= 80:
        grau = "B"
    elif nota >= 70:
        grau = "C"
    elif nota >= 60:
        grau = "D"
    else:
        grau = "E"

    print(nota, grau, end=" || ")
