def main():
    lst = [0 for _ in range(36)]  # [0] * 37

    n = int(input('n: '))
    while not n > 0:
        n = int(input('n: '))

    i = 0
    while i < n:
        v = int(input(f'{i + 1}°: '))
        lst[v] += 1
        i += 1

    i = 0
    print('no.\tfrequências')
    while i < len(lst):
        print(f'{i}\t{lst[i]}')
        i += 1


if __name__ == '__main__':
    main()
