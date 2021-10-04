def hipot(cato, cata):
    return (cato ** 2 + cata ** 2) ** 0.5


def eh_retangulo(a, b, c):
    return a == hipot(b, c) or b == hipot(a, c) or c == hipot(a, b)


print(eh_retangulo(3, 4, 5))
