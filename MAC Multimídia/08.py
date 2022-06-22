def main():
  print('Linha n do Triangulo de Pascal')

  n = int(input('n: '))
  p = pascal(n)

  print(p)


def pascal(n):
  v = [0, 1]
  for i in range(1, n):
    nv = []
    for j in range(1, len(v)):
      nv += [v[j - 1] + v[j]]
    v = [0] + nv + [1]
  
  return v[1:]


main()
