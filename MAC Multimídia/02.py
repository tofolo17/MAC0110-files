def main():
  print('Matriz A')
  n = int(input('n (número de coeficientes): '))
  m = int(input('m (número de equações): '))
  A = le_matriz(m, n)

  print('\nVetor B')
  B = le_vetor(m)

  print('\nVetor X')
  X = le_vetor(n)

  _B = multiplica(A, X)

  if _B != B:
    print('\nNão é solução!')
  else:
    print('\nÉ solução!')


def le_matriz(m, n):
  A = []
  for i in range(m):
    L = []
    for j in range(n):
      v = float(input(f'A{i + 1}{j + 1}: '))
      L += [v]
    A.append(L)
  
  return A


def le_vetor(n):
  V = []
  for i in range(n):
    c = float(input(f'{i + 1}° componente: '))
    V += [c]
  
  return V


def multiplica(A, V):
  C = []
  for L in A:
    r = 0
    for i in range(len(L)):
      r += L[i] * V[i]
    C += [r]
  
  return C


main()
