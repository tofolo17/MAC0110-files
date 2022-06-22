def insere_01(elemento, conjunto: list) -> None:  # Minha interpretação
    if elemento not in conjunto:
        conjunto += [elemento]


def insere_02(elemento, conjunto: list) -> None:  # Interpretação da aula
    i = 0
    while i < len(conjunto):
        if elemento == conjunto[i]:
            return
        i += 1
    conjunto.append(elemento)
