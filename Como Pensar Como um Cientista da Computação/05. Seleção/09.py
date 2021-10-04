def eh_par(n):
    return n % 2 == 0


def eh_impar(n):
    return not (eh_par(n))


print(eh_par(2))
print(eh_par(3))
print(eh_impar(2))
print(eh_impar(3))
