n = 1000

factor = 2 / n
vertical_segment = c = 0
while vertical_segment < 2:
    vertical_segment += factor
    x = vertical_segment - factor / 2

    horizontal_segment = 0
    while horizontal_segment < 2:
        horizontal_segment += factor
        y = horizontal_segment - factor / 2

        dx = 1 - x
        dy = 1 - y

        d = (dx ** 2 + dy ** 2) ** (1 / 2)

        if d <= 1:
            c += 1

pi = 4 * c / (n ** 2)

print(pi)
