def alternante(n):
    if not n > 0:
        n = -n

    spar = 0
    simpar = 0

    i = 1
    while n != 0:
        alg = n % 10
        n = n // 10

        if i % 2 == 0:
            spar += alg
        else:
            simpar += alg

        i += 1

    return spar == simpar


print(alternante(121))
