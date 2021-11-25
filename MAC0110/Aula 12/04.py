"""
Pense em um número inteiro positivo N entre 1 e 100.
Faça um algoritmo que advinhe qual o número pensado com o menor número de perguntas possível.
"""
r = 100
ll = t = 0
acertou = False
while not acertou:
    m = (ll + r) // 2
    resp = int(input(f"{m}? "))

    if resp == 0:
        print(f"Oba, {t} tentativas.")
        acertou = True
    elif resp == 1:
        ll = m + 1
    elif resp == -1:
        r = m - 1

    t += 1
