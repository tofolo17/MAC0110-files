import random

v = [random.randint(1, 10) for _ in range(0, random.randint(1, 10))]
i = 0

while i < len(v) - 1:
    j = i + 1
    while j < len(v):
        if v[i] > v[j]:
            temp = v[i]
            v[i] = v[j]
            v[j] = temp
        j += 1
    i += 1
