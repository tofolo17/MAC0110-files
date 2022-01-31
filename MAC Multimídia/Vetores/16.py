def main():
  k = 8  # int(input('k > 0: '))
  seq = [7, 9, 5, 4, 5, 4, 8, 6]  # populate(k)

  for j in range(2, k // 2 + 1):
    i = 0
    achou = False
    while i + 2 * j <= k and not achou:
      a = seq[i: i + j]
      p = seq[i + j: i + 2 * j]
      if a == p:
        achou = True
        print(i + 1, j)
      i += 1


def populate(n):
  lista = []
  for i in range(n):
    v = int(input(f'x{i + 1}: '))
    lista += [v]
  
  return lista


main()
