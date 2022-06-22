x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

x3 = int(input('x3: '))
y3 = int(input('y3: '))

d12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
d13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
d23 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5

isosceles = False
if d12 == d13 or d12 == d23 or d13 == d23:
    isosceles = True

print(isosceles)
