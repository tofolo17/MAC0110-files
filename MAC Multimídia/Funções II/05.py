def main():
    print('Strings em maíusculo de sequência de n caractéres')
    n = int(input('n > 0: '))

    final_string = ""
    for i in range(1, n + 1):
        v = input(f'{i}° termo: ')
        v_type, upper_v = converte(v)
        if v_type == 1:
            final_string += upper_v + " "

    print(final_string)


def converte(ch):
    if ch.isnumeric():
        return 0, ch
    elif ch.isalpha():
        return 1, ch.upper()
    else:
        return 2, ch


main()
