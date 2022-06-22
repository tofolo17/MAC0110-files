from random import randint

v = [randint(1, 10) for _ in range(0, randint(1, 10))]
i = 0

print(v, len(v))

while i < len(v) - 1:
    j = i + 1
    while j < len(v):
        if v[i] > v[j]:
            temp = v[i]
            v[i] = v[j]
            v[j] = temp
        j += 1
    i += 1
