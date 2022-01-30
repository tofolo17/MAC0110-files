def main():
    print('Contador de palavra em frase')

    frase = input('Frase: ')
    palavra = input('Palavra: ')

    c = 0
    for p in frase.split():
        if palavra == p:
            c += 1

    print(f"'{palavra}' aparece {c} vezes em {frase}")


main()
