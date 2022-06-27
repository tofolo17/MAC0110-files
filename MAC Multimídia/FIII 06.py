def boardV(B):
    s = 0
    for i in range(8):
        for j in range(8):
            p = B[i][j]
            s += power(p)

    return s


def power(p):
    if p == '':
        return 0
    elif p == 'peão':
        return 1
    elif p in ['cavalo', 'bispo']:
        return 3
    elif p == 'torre':
        return 5
    elif p == 'rainha':
        return 10
    elif p == 'rei':
        return 50
