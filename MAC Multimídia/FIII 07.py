def main():
    A = [2, 3, 3, 4]
    B = [2, 3, 3, 4]

    print(contido(A, B), contido(B, A))
    print(iguais(A, B))


def contido(A, B):
    i, j = len(A), len(B)
    if i > j:
        return False

    for k in range(i - 1, j + 1):
        seg = B[k - i: k]
        if seg == A:
            return True

    return False


def iguais(A, B):
    return contido(A, B) and contido(B, A)


main()
