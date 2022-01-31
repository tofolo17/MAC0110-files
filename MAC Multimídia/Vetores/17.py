def main():
  n = int(input('n > 0: '))
  seq = populate(n)

  m = 0
  for j in range(len(seq), 1, -1):
    for i in range(j):
      seg = seq[i:j]
      s = sum(seg)
      if s > m:
        m = s
  print(m)


def populate(n):
  lista = []
  for i in range(n):
    v = int(input(f'{i + 1}° elemento: '))
    lista += [v]
  
  return lista


main()
