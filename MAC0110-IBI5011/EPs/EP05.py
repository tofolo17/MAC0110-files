# Resoluções: https://www.ime.usp.br/~coelho/provas-intro/P1-2013-mac2166.html.

n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

a = 1
eh_soma = False
while a < n // 3 and not eh_soma:
    b = a + 1

    while b <= (n - a) // 2 and not eh_soma:
        c = n - a - b
        print(a, b, c)

        if a ** 2 + b ** 2 == c ** 2:
            eh_soma = True
        b += 1
    a += 1

print(eh_soma)
