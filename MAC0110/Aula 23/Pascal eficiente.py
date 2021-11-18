def fibonacci(n: int) -> list:
    """
    Função que retorna uma lista com os números da sequência de Fibonacci de 1 até n.
    Desenvolvida sem querer.
    """
    v = [1]
    i = j = 0
    while i < n:
        temp = v[i]
        v += [j + v[i]]
        j = temp

        i += 1

    return v
