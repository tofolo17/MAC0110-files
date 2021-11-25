n = int(input())

i = 0
rec = 0
while i < n:
    nota_aluno = float(input())
    if 3 <= nota_aluno < 5:
        rec += 1
    i += 1

print(rec)
