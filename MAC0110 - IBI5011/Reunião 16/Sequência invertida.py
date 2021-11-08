n = int(input())

lst = []
while n > 0:
    v = float(input())
    lst = [v] + lst
    n -= 1

print(lst)
