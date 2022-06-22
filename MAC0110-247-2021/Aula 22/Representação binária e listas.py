n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

v = []
while n > 0:
    v = [str(n % 2)] + v
    n = n // 2

print(''.join(v))
