import random

MAX_TENTATIVAS = 6
NUM_LETRAS = 5


def main():
    lingua = ''
    while lingua != 'P' and lingua != 'I':
        lingua = input("Qual o idioma (I para inglês ou P para português)? ")

    if lingua == 'P':
        lista_palavras = cria_lista_palavras('palavras.txt')
    else:
        lista_palavras = cria_lista_palavras('words.txt')

    palavra = lista_palavras[random.randint(0, len(lista_palavras) - 1)]
    num_tentativas = 0
    lista_tentativas = []
    ganhou = False
    teclado = inicializa_teclado()

    while num_tentativas < MAX_TENTATIVAS and not ganhou:
        marca = 5 * [0]
        chute = input('Digite a palavra: ')
        tentativas = [chute, marca]
        lista_tentativas.append(tentativas)
        for tentativa in lista_tentativas:
            checa_tentativa(palavra, tentativa, marca)
            imprime_resultado(marca[:])
            if marca == [1, 1, 1, 1, 1]:
                ganhou = True
            else:
                print('\n')
            atualiza_teclado(chute, marca[:], teclado)
            imprime_teclado(teclado)
        num_tentativas += 1
    if ganhou:
        print("PARABÉNS!")
    else:
        print("Que pena... A palavra era ", palavra, ".")


##### BLOCO DAS FUNÇÕES TENTATIVA

def cria_lista_palavras(nome_arquivo):
    ''' recebe uma string com o nome do arquivo e devolve uma lista
        contendo as palavras do arquivo'''
    with open(nome_arquivo) as arquivo:
        string_palavras = arquivo.read()
    lista_palavras = string_palavras.split('\n')
    return lista_palavras


def checa_tentativa(palavra, chute, marca):
    ''' Recebe a palavra secreta e o chute do usuario
        e verifica se tem letra certa no lugar certo, atualizando
        a posicao da lista marca correspondente com 1 (verde) e
        se tem letra certa no lugar errado, atualizando a posicao da lista
        marca com 2 (amarelo). '''

    palavra_parcial = palavra[:]

    for i in range(len(chute)):
        j = 0
        while j < len(palavra):
            letra_igual = False
            c = chute[i]
            p = palavra_parcial[j]
            if c == p:
                letra_igual = True
                p = '-'
            elif (c in 'àáãâäå' and p in 'àáãâäå') or (c in 'èéêë' and p in 'èéêë') or (
                    c in 'ìíîï' and p in 'ìíîï') or (c in 'òóõôö' and p in 'òóõôö') or (
                    c in 'ùúûü' and p in 'ùúûü') or (c in 'Çç' and p in 'Çç'):
                letra_igual = True
                p = '-'
            elif letra_igual and i == j and letra_so_uma_vez:
                marca[i] = 1
            elif letra_igual and i != j and letra_so_uma_vez:
                marca[i] = 2
            j += 1


def imprime_resultado(lista):
    ''' Recebe a lista de tentativas e imprime as tentativas,
        usando * para verde e + para amarelo. '''
    for i in range(len(lista)):
        print(lista[i][0])
        u = lista[i][1]
        for j in range(5):
            if valor == 0:
                valor = '_'
            elif valor == 1:
                valor = '*'
            elif valor == 2:
                valor = '+'
        print(valor, end=' ')


###### BLOCO DAS FUNÇÕES TECLADO

def inicializa_teclado():
    ''' Devolve a lista com as teclas na ordem.
        As letras que aparecem nos chutes e que não estão no teclado são substtuídas por ' '.   '''

    teclado = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
               ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    return teclado


def imprime_teclado(teclado):
    ''' Exibe o teclado com as letras possiveis. '''
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end=' ')
        print()
    print('-----------------------------------------')


def atualiza_teclado(chute, marca, teclado):
    for i in range(len(marca)):
        if marca[i] == 0:
            letra_fora = chute[i]
            for linha in teclado:
                for letra in linha:
                    if letra_fora == letra:
                        letra = ' '
    ''' Modifica teclado para que as letras marcadas como inexistentes
        no chute sejam substituidas por espacos. '''


if __name__ == "__main__":
    main()
