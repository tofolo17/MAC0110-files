def main():
    linhas = pega_linhas(filename="Texto mais frequente")
    moda = moda_string(linhas)
    print(moda)


def pega_linhas(filename):
    with open(file=filename, mode='r', encoding='utf-8') as f:
        text = f.read()

    return text.split(sep='\n')


def separa(linha, seps):
    linha += " "

    palavras = []
    inicio = fim = 0

    while fim < len(linha):
        char = linha[fim]
        if char in seps:
            if fim > inicio:
                palavras.append(linha[inicio: fim])
            inicio = fim + 1

        fim += 1

    return palavras


def moda_string(linhas):
    seps = " ,.;:[](){}!?'\""  # Teremos problema com apóstrofes e palavras compostas com hífe, por exemplo)
    p_unicas, contador = [], []

    for i in range(len(linhas)):
        linha = linhas[i]

        palavras = separa(linha, seps)
        print(palavras)

        for j in range(len(palavras)):
            palavra = palavras[j]

            if len(palavra) > 3:
                if palavra in p_unicas:
                    idx = p_unicas.index(palavra)
                    contador[idx] += 1
                else:
                    p_unicas += [palavra]
                    contador += [1]

    idx = contador.index(max(contador))
    return p_unicas[idx], contador[idx]


main()
