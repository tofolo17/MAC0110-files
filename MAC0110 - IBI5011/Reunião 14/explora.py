import harmonico as ha


def main():
    fim = 100
    n = 1
    difs = 0
    while n <= fim:
        d, e = ha.hde(n)
        if d != e:
            difs += 1
            print(d, e, abs(d - e))
        n += 1

    print(difs)


main()
