# b)
def main():
    """n = int(input('n: '))

    seq = []
    for i in range(n):
      t = int(input(f'Tamanho do conjunto {i + 1}: '))
      conj = [t]

      for i in range(t):
        v = int(input(f'{i + 1}° número: '))
        conj += [v]

      seq.append(conj)"""

    seq = [
        [4, 1, 3, 3, 5],
        [3, 3, 2, 5],
        [1, 5]
    ]

    I = seq[0]
    for i in range(1, len(seq)):
        I = intersec(I, seq[i])

    print(I)


# a)
def intersec(A, B):
    C = []
    for el in A[1:]:
        if el in B[1:]:
            C += [el]

    return [len(C)] + C


main()
