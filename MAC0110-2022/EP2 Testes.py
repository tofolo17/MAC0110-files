MAX_TENTATIVAS = 6
NUM_LETRAS = 5


def main():
    chute = 'piada'
    teclado = inicializa_teclado()

    marca = [0, 0, 0, 0, 0]

    atualiza_teclado(chute, marca, teclado)

    print(teclado)


def cria_lista_palavras(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        string_palavras = arquivo.read()
    lista_palavras = string_palavras.split('\n')
    return lista_palavras


def checa_tentativa(palavra, chute, marca):
    lista_chute = list(chute[:])
    lista_palavra = list(palavra[:])

    chute_normal = normaliza(lista_chute)
    palavra_normal = normaliza(lista_palavra)

    for i in range(5):
        if chute_normal[i] == palavra_normal[i]:
            marca[i] = 1
            chute_normal[i] = '_'
            palavra_normal[i] = '_'

    for i in range(5):
        if chute_normal[i] in lista_palavra:
            marca[i] = 2
            chute_normal[i] = '_'
            palavra_normal[i] = '_'

    for i in range(5):
        if chute_normal[i] != '_':
            marca[i] = 0

    print(marca, chute_normal, palavra_normal)


def imprime_resultado(lista):
    for i in range(len(lista)):
        print(lista[i][0])
        for j in range(5):
            if lista[i][1][j] == 0:
                lista[i][1][j] = '_'
            elif lista[i][1][j] == 1:
                lista[i][1][j] = '*'
            elif lista[i][1][j] == 2:
                lista[i][1][j] = '+'
        for character in lista[i][1]:
            print(character, end=' ')
        print('')


def atualiza_teclado(chute, marca, teclado):
    print(teclado)
    for i in range(5):
        if marca[i] == 0:
            for linha in teclado:
                for j in range(len(linha)):
                    if chute[i] == linha[j]:
                        linha[j] = ' '

    print(teclado)


def inicializa_teclado():
    teclado = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

    return teclado


def imprime_teclado(teclado):
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end=' ')
        print()
    print('-----------------------------------------')


# Funções autorais
def normaliza(palavra):
    palavra_normal = list(palavra)
    for i in range(5):
        letra = palavra_normal[i]
        if letra in 'àáãâäå':
            palavra_normal[i] = 'a'
        elif letra in 'èéêë':
            palavra_normal[i] = 'e'
        elif letra in 'ìíîï':
            palavra_normal[i] = 'i'
        elif letra in 'òóõôö':
            palavra_normal[i] = 'o'
        elif letra in 'ùúûü':
            palavra_normal[i] = 'u'
        elif letra == 'ç':
            palavra_normal[i] = 'c'

    return palavra_normal


if __name__ == "__main__":
    main()
