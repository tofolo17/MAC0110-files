"""
Dado um inteiro positivo  N  e uma sequência com  M  notas finais de MAC0110-247-2021, determine quantos alunos:
foram aprovados:  notafinal≥5 ;
estão de recuperação:  3≤notafinal<5 ;
foram reprovados:  notafinal<3 .
"""
m = int(input())

i = aprovados = reprovados = rec = 0
while i < m:
    n = float(input())
    if n >= 5:
        aprovados += 1
    elif 3 <= n < 5:
        rec += 1
    else:
        reprovados += 1
    i += 1

print(aprovados, reprovados, rec)
