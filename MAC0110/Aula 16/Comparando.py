def gp_mean(n, a_0, q):
    cont = s = 0
    while cont < n:
        termo = q ** cont * a_0
        s += termo
        cont += 1

    return s / n


def gp_mean_2(n, a_0, q):
    s = a_0 * ((q ** n - 1) / (q - 1))

    return s / n


print(gp_mean(3, 2, 2) == gp_mean_2(3, 2, 2))
