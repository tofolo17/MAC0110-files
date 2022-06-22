def main():
  print('Matriz A n-por-n é um quadrado mágico?\n')

  n = int(input('Número de linhas e colunas da matriz A: '))
  A = le_matriz(n, n)

  r = quad_magico(A, n)
  print(f'Resposta: {r}')


def quad_magico(A, n):
  p, s = 0, 0
  for i in range(n):
    L = A[i]
    C = [A[j][i] for j in range(n)]

    if sum(L) != sum(C):
      return False
    
    s += L[i]
    p += L[n - 1 - i]

  if s != p:
    return False
  
  return True


def le_matriz(m, n):
  A = []
  for i in range(m):
    L = []
    for j in range(n):
      v = int(input(f'A{i + 1}{j + 1}: '))
      L += [v]
    A.append(L)
  
  return A


main()
