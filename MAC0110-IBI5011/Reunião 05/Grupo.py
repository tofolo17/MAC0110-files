x = float(input())
y = float(input())

hit = True
if -4 <= x <= 6 and 2 <= y <= 10:
    # Dentro do retângulo.
    if -2 <= x <= 4 and 3 <= y <= 9:
        # Dentro do quadrado do perigo.
        if 2 < x < 4 and 7 < y < 9:
            # Dentro do quadrado aberto superior direito.
            hit = False
        if -2 <= x <= 1 and 3 <= y <= 9:
            # Dentro do retângulo mais alto que contém o pequeno alvo.
            if not (-1 <= x <= 0 and 4 <= y <= 5):
                # Se não estiver dentro do pequeno alvo.
                hit = False
        if 1 < x <= 4 and 3 <= y <= 6:
            # Dentro do quadrado inferior direito.
            hit = False

else:
    # Fora do retângulo.
    hit = False

if hit:
    print("Dentro")
else:
    print("Fora")
