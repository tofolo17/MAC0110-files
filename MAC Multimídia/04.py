def main():
  print('Matriz A tem elementos repetidos?\n')

  m = int(input('Número de linhas de A: '))
  n = int(input('Número de colunas de A: '))
  A = le_matriz(m, n)

  print(tem_repetido(A))


def le_matriz(m, n):
  A = []
  for i in range(m):
    L = []
    for j in range(n):
      v = float(input(f'A{i + 1}{j + 1}: '))
      L += [v]
    A.append(L)
  
  return A


def tem_repetido(A):
  presentes = []
  for linha in A:
    for el in linha:
      if el in presentes:
        return True
      presentes += [el]
  
  return False


main()
