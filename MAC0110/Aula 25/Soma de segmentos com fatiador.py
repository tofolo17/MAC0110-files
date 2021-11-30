def main():
    v = [1, 5, -3, 7, 6, -13, 22]

    m = 0
    for i in range(len(v)):
        for j in range(i, len(v)):
            v_fatiada = v[i:j + 1]
            s = sum(v_fatiada)
            if s > m:
                m = s

    print(m)


main()
