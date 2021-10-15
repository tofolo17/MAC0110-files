def factorial(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1

    return r


def binomial(n, m):
    coef = factorial(m) / (factorial(m - n) * factorial(n))

    return coef


def expansion(n):
    i = 0
    while i <= n:
        print(round(binomial(n, i), 4), end=" ")
        i += 1


print(factorial(4))
print(binomial(2, 4))
expansion(4)
