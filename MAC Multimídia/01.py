def main():
  print('Matriz A')
  n = int(input('n (colunas): '))
  m = int(input('m (linhas): '))
  A = le_matriz(m, n)

  print('\nVetor V')
  V = le_vetor(n)

  C = multiplica(A, V)
  print(f'\nMultiplicação A x V: {C}')


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
