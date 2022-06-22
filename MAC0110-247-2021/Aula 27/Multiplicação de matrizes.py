def main():
    A = [
        [12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]
    ]

    print(multiplica_matriz(A, B))


def multiplica_matriz(A, B):
    m = len(A)
    n = len(B[0])

    p = len(A[0])  # ou len(B)

    # A é m-por-p
    for i in range(m):

        # B é p-por-n
        for j in range(n):

            s = 0
            for k in range(p):
                s += A[i][k] * B[k][j]

            print(s)


main()
