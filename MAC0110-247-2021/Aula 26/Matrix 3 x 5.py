m = []

for i in range(3):
    m.append([])  # o método append deve ser usado, e não o operador +
    for j in range(5):
        m[i] += [0]

m[0][1] = 2
for i in range(3):
    for j in range(5):
        print(m[i][j], end=' ')
    print()
