def eh_bissexto(ano):
    result = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        result = True

    return result


print(eh_bissexto(2020))
