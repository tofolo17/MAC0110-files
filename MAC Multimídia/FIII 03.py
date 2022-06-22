def main():
  A = [
      [2, 3, 6],
      [-2, 4, 2]
  ]

  print(soma_linha(A, 0), prod_coluna(A, 1))


def soma_linha(A, i):
  s = 0
  for el in A[i]:
    s += el

  return s


def prod_coluna(A, j):
  p = 1
  for L in A:
    p *= L[j]
  
  return p


main()

