def main():
    print("Teste soma()")
    lst = [1, -1, 4]
    print(f"soma({lst}) = {soma(lst)}")
    lst = [-2.1, 1.3]
    print(f"soma({lst}) = {soma(lst)}")
    lst = []
    print(f"soma({lst}) = {soma(lst)}")

    print("\nTeste fatia()")
    lst = [-1, 23, 'oi', True, 2.71, None, 45]
    print(f"fatia({lst}, 0, {len(lst)}) = {fatia(lst, 0, len(lst))}")
    print(f"fatia({lst}, 2, 5)) = {fatia(lst, 2, 5)}")
    print(f"fatia({lst}, 3, 7)) = {fatia(lst, 3, 7)}")
    print(f"fatia({lst}, 4, 4)) = {fatia(lst, 4, 4)}")


def soma(lst):
    # return sum(lst)
    s = 0
    for element in lst:
        s += element

    return s


def fatia(lst, ini, fim):
    # return lst[ini:fim]
    sublst = []
    for i in range(ini, fim):
        sublst += [lst[i]]

    return sublst


# inicio do programa
if __name__ == "__main__":
    main()
