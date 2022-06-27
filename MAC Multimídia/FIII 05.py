def main():
    A = [
        [2, 3, 6],
        [2, 4, 2],
        [4, 2, 5]
    ]
    n = 3

    print('M\tL\tC')
    for i in range(n * n):
        mel, mi, mj = MAX(n, A)
        print(f'{mel}\t{mi}\t{mj}')
        A[mi][mj] = -1


def MAX(n, A):
    mel, mi, kj = 0, 0, 0
    for i in range(n):
        for j in range(n):
            el = A[i][j]
            if mel < el:
                mel, mi, mj = el, i, j

    return mel, mi, mj


main()
