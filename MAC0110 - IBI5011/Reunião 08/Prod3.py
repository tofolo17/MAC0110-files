n = int(input())

r = 0
i = 3
prod3 = False
while r < n and not prod3:
    r = i * (i - 1) * (i - 2)
    if r == n:
        print(f'Opa!')
        prod3 = True
    i += 1
