n = 5901234123457

s = 0
i = 1
while i < 13 + 1:
    alg = n % 10

    if i % 2 == 1:
        s += alg
    else:
        s += alg * 3

    i += 1
    n = n // 10

print(s % 10)
