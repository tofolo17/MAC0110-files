n = int(input("n: "))
while not n > 0:
    n = int(input("n: "))

i = s = 0
while i < n:
    m = int(input(f"{i + 1} número: "))

    if m > 0:
        s += m

    i += 1

print(f'Soma: {s}')
