def gp_mean(n, a_0, q):
    cont = s = 0
    while cont < n:
        print(f'{q}^{cont} * {a_0}')
        termo = q ** cont * a_0

        print(f'{s} + {termo} = {s + termo}\n')
        s += termo

        cont += 1

    return s / n


print(gp_mean(3, 2, 2))
