n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

i = 2
primo = True
while i < n and primo:
    if n % i == 0:
        primo = False
    i += 1

print(primo)
