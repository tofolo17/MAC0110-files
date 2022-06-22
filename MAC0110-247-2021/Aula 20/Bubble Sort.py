from random import randint

v = [randint(1, 10) for _ in range(0, randint(1, 10))]
i = len(v) - 1

while i > 0:
    j = 0
    while j < i:
        if v[j] > v[j + 1]:
            temp = v[j + 1]
            v[j + 1] = v[j]
            v[j] = temp
        j += 1
    i -= 1
