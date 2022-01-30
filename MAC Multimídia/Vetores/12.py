def main():
    # q(x) = p(x) / (x - a) - p(a)
    n = int(input('n: '))
    coefs = popula(n, 'pol')

    m = int(input('m: '))
    alphas = popula(m)

    qxs = q(coefs, alphas)
    print(qxs)


def popula(n, t=None):
    lista = []
    for i in range(n):
        frase = f'a{i}: ' if t == 'pol' else f'{i + 1}° alpha: '
        v = float(input(frase))
        lista += [v]

    return lista


def p(coefs, x):
    px = 0
    for i in range(len(coefs) - 1, -1, -1):
        px += coefs[i] * x ** i

    return px


def q(coefs, alphas):
    qxs = []
    for alpha in alphas:
        qx = [coefs[0]]
        for i in range(1, len(coefs)):
            qx += [coefs[i] + alpha * qx[i - 1]]
        qx[-1] -= p(coefs, alpha)
        qxs.append(qx)
    return qxs


main()
