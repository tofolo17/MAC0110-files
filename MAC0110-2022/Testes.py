def main():
    chute = "marca"
    palavra = "calma"

    chute = [char for char in chute]
    palavra = [char for char in palavra]

    marca = ['_', '_', '_', '_', '_']

    checa_tentativa(palavra, chute, marca)


def checa_tentativa(palavra, chute, marca):
    """
    Recebe a palavra secreta e o chute do usuario
    e verifica se tem letra certa no lugar certo, atualizando
    a posicao da lista marca correspondente com 1 (verde) e
    se tem letra certa no lugar errado, atualizando a posicao da lista
    marca com 2 (amarelo).
    """
    print(chute)
    print(palavra)

    # checa igualdades
    for i in range(len(palavra)):
        c = chute[i]
        p = palavra[i]

        if c == p:
            marca[i] = '1'
            chute[i] = ' '
            palavra[i] = ' '

    # checa "ins"
    for i in range(len(palavra)):
        c = chute[i]

        if c in palavra and c != ' ':
            marca[i] = '2'
            chute[i] = ' '
            palavra[i] = ' '

    # checa desigualdades
    for i in range(len(palavra)):
        c = chute[i]
        p = palavra[i]

        if c != p and c != ' ':
            marca[i] = '0'

    print(marca)


main()
