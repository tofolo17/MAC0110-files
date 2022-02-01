def main():
  print('Matriz A é permutação?\n')

  n = int(input('Número de linhas e colunas da matriz A: '))
  A = le_matriz(n, n)

  i = 0
  eh_permuta = True
  while i < n and eh_permuta:
    L = A[i]
    C = [A[i][j] for j in range(n)]
    print(L, C)

    if not(permuta(L) and permuta(C)):
      eh_permuta = False

    i += 1
  
  print(f'Resposta: {eh_permuta}')


def le_matriz(m, n):
  A = []
  for i in range(m):
    L = []
    for j in range(n):
      v = int(input(f'A{i + 1}{j + 1}: '))
      L += [v]
    A.append(L)
  
  return A


def permuta(V):
  s_0, s_1 = 0, 0
  for el in V:
    if el == 0:
      s_0 += 1
    if el == 1:
      s_1 += 1
  
  return s_0 == len(V) - 1 and s_1 == 1


main()
