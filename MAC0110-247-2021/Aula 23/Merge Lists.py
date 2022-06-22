def main():
    # n = positive_input('n: ')
    n_values = [1, 3, 7, 13, 34, 66, 155, 16666, 23421341]  # populate_sorted_list(n)
    print(n_values)

    # m = positive_input('m: ')
    m_values = [4, 8, 12, 12, 133]  # populate_sorted_list(m)
    print(m_values)

    print(merge_and_sort(n_values, m_values))


def positive_input(message: str) -> int:
    n = int(input(message))
    while not n > 0:
        n = int(input(message))

    return n


def populate_sorted_list(size: int) -> list:
    v = int(input('1° valor: '))
    sorted_list = [v]

    for i in range(1, size):
        v = int(input(f'{i + 1}° valor: '))
        sorted_list += [v]

        while not sorted_list[i] >= sorted_list[i - 1]:
            v = int(input(f'Erro. {i + 1}° valor: '))
            sorted_list[i] = v

    return sorted_list


def merge_and_sort(list_1: list, list_2: list) -> list:
    ms_list = []

    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            ms_list += [list_1[i]]
            i += 1
        else:
            ms_list += [list_2[j]]
            j += 1

    if not i < len(list_1):
        while j < len(list_2):
            ms_list += [list_2[j]]
            j += 1

    if not j < len(list_2):
        while i < len(list_1):
            ms_list += [list_1[i]]
            i += 1

    return ms_list


main()
