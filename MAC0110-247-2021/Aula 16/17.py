def gp_mean(n, a_0, q):
    s = a_0 * ((q ** n - 1) / (q - 1))

    return s / n


print(gp_mean(3, 2, 2))
