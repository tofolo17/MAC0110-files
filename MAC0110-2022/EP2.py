from random import randint

MAX_TENTATIVAS = 6
NUM_LETRAS = 5


def main():
    """ Implementa mecanismo principal do jogo. """
    # pede opção de lingua
    lingua = ''
    while lingua != 'P' and lingua != 'I':
        lingua = input("Qual o idioma (I para inglês ou P para português)? ")

    # carrega lista de palavras do arquivo correspondente
    if lingua == 'P':
        lista_palavras = cria_lista_palavras('palavras.txt')
    else:
        lista_palavras = cria_lista_palavras('words.txt')

    # sorteia uma palavra da lista
    palavra = lista_palavras[randint(0, len(lista_palavras) - 1)]

    # lista para funcionamento e substituições
    subs = {
        'á': 'a',
        'â': 'a',
        'ã': 'a',
        'é': 'e',
        'ê': 'e',
        'í': 'i',
        'ó': 'o',
        'ô': 'o',
        'ú': 'u',
        'ç': 'c'
    }
    palavra_list = []
    for char in palavra:
        if char in subs:
            char = subs[char]
        palavra_list += char

    # variáveis da partida
    ganhou = False
    num_tentativas = 0
    lista_tentativas = []
    teclado = inicializa_teclado()
    marca = ['_', '_', '_', '_', '_']

    # loop do jogo
    while num_tentativas < MAX_TENTATIVAS and not ganhou:
        imprime_teclado(teclado)

        # input do chute
        chute = input('Digite a palavra: ').lower()
        while chute not in lista_palavras:
            print('Palavra inválida!')
            chute = input('Digite a palavra: ').lower()

        # transformação de chute e análise da tentativa
        chute = [char for char in chute]
        checa_tentativa(palavra_list, chute, marca)

        lista_tentativas.append([chute, marca[:]])
        imprime_resultado(lista_tentativas)

        atualiza_teclado(chute, marca, teclado)

        num_tentativas += 1
        if marca == ['1', '1', '1', '1', '1']:
            ganhou = True

    if ganhou:
        print("PARABÉNS!")
    else:
        print("Que pena... A palavra era", palavra, ".")


def cria_lista_palavras(nome_arquivo):
    """
    Recebe uma string com o nome do arquivo e devolve uma lista
    contendo as palavras do arquivo
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read().splitlines()


def inicializa_teclado():
    """
    Devolve a lista com as teclas na ordem.
    As letras que aparecem nos chutes e que não estão no teclado são substtuídas por ' '.
    """
    teclado = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]
    return teclado


def checa_tentativa(palavra, chute, marca):
    """
    Recebe a palavra secreta e o chute do usuario
    e verifica se tem letra certa no lugar certo, atualizando
    a posicao da lista marca correspondente com 1 (verde) e
    se tem letra certa no lugar errado, atualizando a posicao da lista
    marca com 2 (amarelo).
    """
    # evitando alterações fora do escopo
    temp_chute = chute[:]
    temp_palavra = palavra[:]

    # checa igualdades
    for i in range(len(temp_palavra)):
        c = temp_chute[i]
        p = temp_palavra[i]

        if c == p:
            marca[i] = '1'
            temp_chute[i] = ' '
            temp_palavra[i] = ' '

    # checa "ins"
    for i in range(len(temp_palavra)):
        c = temp_chute[i]

        if c in temp_palavra and c != ' ':
            marca[i] = '2'
            temp_chute[i] = ' '
            temp_palavra[i] = ' '

    # checa desigualdades
    for i in range(len(temp_palavra)):
        c = temp_chute[i]

        if c != ' ':
            marca[i] = '_'


def imprime_resultado(lista):
    """
    Recebe a lista de tentativas e imprime as tentativas,
    usando * para verde e + para amarelo.
    """
    for resultados in lista:
        palavra = resultados[0]
        marca = resultados[1]

        for char in palavra:
            print(char, end=' ')
        print()

        for char in marca:
            if char == '1':
                print('*', end=' ')
            elif char == '2':
                print('+', end=' ')
            else:
                print(char, end=' ')
        print()


def imprime_teclado(teclado):
    """ Exibe o teclado com as letras possiveis. """
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end=' ')
        print()
    print('-----------------------------------------')


def atualiza_teclado(chute, marca, teclado):
    """
    Modifica teclado para que as letras marcadas como inexistentes
    no chute sejam substituidas por espacos.
    """
    remover = []
    for i in range(len(marca)):
        if marca[i] == '_':
            remover += [chute[i]]

    for i in range(len(teclado)):
        for j in range(len(teclado[i])):
            if teclado[i][j] in remover:
                teclado[i][j] = ' '


if __name__ == "__main__":
    main()
