"""
n = int(input('n: '))
while not n > 0:
    n = int(input('n: '))

i = 0
values = []
while i < n:
    v = int(input(f'{i + 1}°: '))
    values += [v]
    i += 1
"""


def main():
    v = [1, 3, -3, 4, -7, 8, 10, -64]

    m = 0
    for i in range(len(v)):
        for j in range(i, len(v)):

            s = soma(v, i, j)
            if s > m:
                m = s

    print(f'\n{m}')


def soma(values, start, end):
    s = 0
    for i in range(start, end + 1):
        print(f'{values[i]}', end=' ')
        s += values[i]
    print(f'= {s}')

    return s


main()
