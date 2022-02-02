def main():
  A = [
      [2, 3, 6],
      [-2, 4, 2]
  ]

  A = troca_linha(A, 0, 1)
  print(A)


def troca(a, b):
  return b, a


def troca_linha(A, i, j):
  A[i], A[j] = troca(A[i], A[j])
  
  return A


main()
