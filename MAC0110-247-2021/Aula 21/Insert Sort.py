from random import randint

v = [randint(1, 10) for _ in range(0, randint(1, 10))]

i = 1
while i < len(v):
    j = i
    trocou = False
    while j >= 1 and not trocou:
        if v[j] < v[j - 1]:
            temp = v[j - 1]
            v[j - 1] = v[j]
            v[j] = temp
            trocou = True
        j -= 1
    i += 1

print(v)
