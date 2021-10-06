def newton_sqrt(n, howmany):
    better_approx = 0
    approx = 0.5 * n
    for i in range(howmany):
        better_approx = 0.5 * (approx + n / approx)

        print(f'Melhor: {better_approx}')

        approx = better_approx
    return better_approx


print(newton_sqrt(10, 25))
