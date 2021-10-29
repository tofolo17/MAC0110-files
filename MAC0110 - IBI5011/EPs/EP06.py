# ----------------------------------------------------
def primo(n):
    """(int) -> bool

       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    """
    if n != 2 and n % 2 == 0:
        eh_primo = False
    else:
        i = 3
        eh_primo = True
        while i < n // 2 and not eh_primo:
            if n % i == 0:
                eh_primo = False
            i += 2

    return eh_primo


# ----------------------------------------------------
def goldbach(n):
    """(int) -> bool, int, int

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    """


# ----------------------------------------------------
def exponencial(n0, e, p, d):
    """(int, int, float, int) -> int

       RECEBE

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0.

      RETORNA o número total de indivíduos infectados até o dia d
      determinado por (n0, e, p).
    """
    print("Vixe! Ainda não fiz a função exponencial()")


# --------------------------------------------------
def logistica(n0, e, p, n, d):
    """(int, int, float, int, int) -> int

       RECEBE

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0.

       RETORNA o número total de indivíduos infectados até o dia d
       determinado por (n0, e, p, n).

    """
    print("Vixe! Ainda não fiz a função logistica()")
