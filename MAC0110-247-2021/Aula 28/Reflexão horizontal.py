def main():
    M = [
        [0, 0, 0, 1],
        [0, 0, 2, 1],
        [0, 3, 2, 1],
        [4, 3, 2, 1]
    ]

    M = reflexao_horizontal(M)
    print(M)


def reflexao_horizontal(matriz):
    M = [matriz[i - 1] for i in range(len(matriz), 0, -1)]
    return M


main()
