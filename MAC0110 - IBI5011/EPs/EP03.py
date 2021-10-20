# Pode não estar 100% correto
coords = [[-10, 10], [2, 7.75], [2, 7], [2, 6.5], [1, 1], [7.5, 0.5], [2, 2.5], [2, 4], [4.5, 4], [8, 8], [5, 7.75],
          [6, 7.25]]

for coord in coords:
    x = coord[0]
    y = coord[1]

    # Sistema visível
    dentro = False
    if 0 <= x <= 8 and 0 <= y <= 8:
        dentro = True

    # Retângulos
    na_bochecha = (x < 1 or x > 7) and y < 2
    na_sobrancelha = 7.25 <= y <= 7.75 and (1 <= x <= 3 or 5 <= x <= 7)
    no_nariz = 3.5 <= x <= 4.5 and 3.5 <= y <= 4.5

    if na_bochecha or na_sobrancelha or no_nariz:
        dentro = False

    # Circunferências
    d_olho_1 = (x - 2) ** 2 + (y - 6) ** 2
    d_olho_2 = (x - 6) ** 2 + (y - 6) ** 2
    no_olho = 0.5 < d_olho_1 <= 1 or 0.5 < d_olho_2 <= 1

    d_boca_1 = (x - 3) ** 2 + (y - 2) ** 2
    d_boca_2 = (x - 5) ** 2 + (y - 2) ** 2
    na_boca = d_boca_1 < 0.5 or d_boca_2 < 0.5 or (3 <= x <= 5 and 1.5 < y < 2.5)

    if dentro and (no_olho or na_boca):
        dentro = False

    if dentro:
        print('azul')
    else:
        print('branco')
