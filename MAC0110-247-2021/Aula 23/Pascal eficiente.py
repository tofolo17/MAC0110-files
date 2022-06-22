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


def pascal(n: int) -> list:
    v = [1]
    if n != 0:
        v += [1]
        i = 1
        while i < n:
            j = 1
            v_temp = []
            while j < len(v):
                v_temp += [v[j] + v[j - 1]]
                j += 1
            v = [1] + v_temp + [1]
            i += 1

    return v


print(pascal(4))
