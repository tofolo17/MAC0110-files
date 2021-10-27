n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

a = 1
eh_soma = False

"""
# Essa solução já é decente, mas podemos melhorá-la
while a < n:
    b = a + 1
    while b < n:
        c = b + 1
        while c ** 2 < a ** 2 + b ** 2:
            c += 1
        if a ** 2 + b ** 2 == c ** 2 and a + b + c == n:
            eh_soma = True
        b += 1
    a += 1
"""

print(eh_soma)
