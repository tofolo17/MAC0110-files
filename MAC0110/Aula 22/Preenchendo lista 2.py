values = []
n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

while n > 0:
    v = int(input('v: '))
    values.append(v)
    n -= 1

print(values)
