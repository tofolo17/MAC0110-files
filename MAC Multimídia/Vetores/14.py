n = 5

num = [0, 1]
den = [1, 1]
while max(den) <= 5:
    nova_num = []
    nova_den = []

    for j in range(len(den) - 1):
        nova_num += [num[j], num[j] + num[j + 1]]
        nova_den += [den[j], den[j] + den[j + 1]]

    nova_num += [num[-1]]
    nova_den += [den[-1]]

    num = nova_num
    den = nova_den

for i in range(len(num)):
    if den[i] <= 5:
        print(f'{num[i]}/{den[i]}')
