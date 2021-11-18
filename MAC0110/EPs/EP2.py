"""
https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
https://pandas.pydata.org/docs/index.html
"""
from math import sqrt
from random import random

import matplotlib.pyplot as plt
from pandas import read_csv


def main():
    SimulaConvergenciaPi(10, 100, 100)

    dados = leiaDados('Dados EP2.csv')
    print(calculaPi(dados))


def mediaV(V: list, n: int) -> float:
    """
    :param V: Lista de valores numéricos;
    :param n: Número de elementos em 'V';
    :return: Média de 'V'.
    """
    s = i = 0
    while i < n:
        s += V[i]
        i += 1

    return s / n


def varV(V: list, n: int) -> float:
    """
    :param V: Lista de valores numéricos;
    :param n: Número de elementos em 'V';
    :return: Variância de 'V'.
    """
    m = mediaV(V, n)
    s = i = 0
    while i < n:
        s += (V[i] - m) ** 2
        i += 1

    return s / (n - 1)


def PiMCM(n: int) -> float:
    """
    :param n: Número de pontos aleatórios criados;
    :return: Estimativa de PI. Número de pontos que caíram dentro do semi-círculo, dividido por 'n'.
    """
    s = i = 0
    while i < n:
        rx = random()
        ry = random()
        d = sqrt(rx ** 2 + ry ** 2)
        if d <= 1:
            s += 1
        i += 1

    return (s / n) * 4


def estimaPiMC(r: int, n: int) -> (float, float):
    """
    :param r: Número de simulações;
    :param n: Número de pontos aleatórios criados em cada simulação;
    :return: Média e variância dos resultados das simulações.
    """
    i = 0
    simulations = []
    while i < r:
        sim = PiMCM(n)
        simulations += [sim]
        i += 1

    return mediaV(simulations, r), varV(simulations, r)


def SimulaConvergenciaPi(m: int, r: int, n: int):
    """
    :param m: Número de simulação maiores de simulações de Monte Carlo;
    :param r: Número de simulações de Monte Carlo;
    :param n: Número de pontos aleatórios criados em cada simulação de Monte Carlo.
    """
    i = 0
    medias, dps = [], []
    while i < m:
        me, v = estimaPiMC(r, n)
        medias += [me]
        dps += [sqrt(v)]
        i += 1

    """
    Até aqui, tudo perfeito.
    """

    GraficaMCMPi(medias, dps, m)


def GraficaMCMPi(mediaMCMPi: list, desvioMCMPi: list, m: int):
    """
    Obs.: não sei se devo mesmo usar um parâmetro adicional 'm'.

    :param mediaMCMPi: Lista das médias de cada simulação maior;
    :param desvioMCMPi: Lista dos desvios padrões de cada simulação maior;
    :param m: Número de elementos em 'mediaMCMPi'.
    """
    xticks = range(1, m + 1)

    plt.errorbar(xticks, mediaMCMPi, yerr=desvioMCMPi, fmt='o')

    plt.xticks(xticks)
    plt.xlabel("Simulações")

    plt.ylabel("Valores")

    plt.title("Simulação da convergência de Pi")  # Rever título
    plt.show()


def leiaDados(filename: str):
    """
    :param filename: Nome do arquivo a ser lido;
    :return: Objeto contendo os dados do arquivo.
    """
    dados = read_csv(filename, sep=';')

    return dados


def calculaPi(dados) -> list:
    """
    :param dados: Objeto semelhante a uma planilha. Deve conter colunas 'diametro' e 'circunferencia';
    :return: Uma lista com o valor de 'circunferencia' / 'diametro' para cada linha de 'dados'.
    """
    i = 0
    pis = []
    while i < len(dados):
        pis += [dados['circuferencia'][i] / dados['diametro'][i]]
        i += 1

    return pis


def estimavaMediaPi(valoresPi: list) -> (float, float):
    """
    :param valoresPi: Lista de valores aproximados de Pi;
    :return: Média e variância de 'valoresPi'.
    """
    size = len(valoresPi)
    return mediaV(valoresPi, size), varV(valoresPi, size)


"""
E a assinatura do E10?
"""
main()
