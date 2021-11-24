"""
https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
https://pandas.pydata.org/docs/index.html
"""
from math import sqrt
from random import random

import matplotlib.pyplot as plt
import pandas


def main():
    SimulaConvergenciaPi(m=50, n=2000, r=10)

    dados = leiaDados('Dados EP2.csv')
    values_pi = calculaPi(dados)
    melhoraPi(values_pi)


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

    GraficaMCMPi(m, medias, dps)


def GraficaMCMPi(mpontos: int, mediaMCMPi: list, desvioMCMPi: list) -> None:
    """
    :param mediaMCMPi: Lista das médias de cada simulação maior;
    :param desvioMCMPi: Lista dos desvios padrões de cada simulação maior;
    :param mpontos: Número de elementos em 'mediaMCMPi'.
    """
    xticks = range(1, mpontos + 1)

    plt.errorbar(xticks, mediaMCMPi, yerr=desvioMCMPi, fmt='o')

    plt.xticks(xticks, rotation=-90, fontsize=7)
    plt.xlabel("Simulações")

    plt.ylabel("Valores")

    plt.title("Convergência - π")
    plt.savefig('GraficaMCMPi')


def leiaDados(filename: str):
    """
    :param filename: Nome do arquivo a ser lido;
    :return: Objeto contendo os dados do arquivo.
    """
    dados = pandas.read_csv(filename, sep=';')

    return dados


def calculaPi(dados) -> list:
    """
    :param dados: Objeto semelhante a uma planilha. Deve conter colunas 'diametro' e 'circunferencia';
    :return: Uma lista com o valor de 'circunferencia' / 'diametro' para cada linha de 'dados'.
    """
    i = 0
    pis = []
    while i < len(dados):
        pis += [dados['circunferencia'][i] / dados['diametro'][i]]
        i += 1

    return pis


def estimavaMediaPi(valoresPi: list) -> (float, float):
    """
    :param valoresPi: Lista de valores aproximados de Pi;
    :return: Média e variância de 'valoresPi'.
    """
    size = len(valoresPi)
    return mediaV(valoresPi, size), varV(valoresPi, size)


def E10(dados) -> None:
    """
    Falta assinatura apropriada.
    """
    plt.scatter(dados['circunferencia'], dados['diametro'])

    plt.xlabel("Circunferência (cm)")
    plt.ylabel("Diâmetro (cm)")

    plt.title("Relação circunferência x diâmetro das medidas")

    plt.show()


def GraficaPiEstimado(valoresPi: list) -> None:
    """
    :param valoresPi: Lista de valores aproximados de Pi.
    """
    x = range(1, len(valoresPi) + 1)

    plt.scatter(x, valoresPi)

    plt.xlabel("Índice")
    plt.ylabel("Valores de π")

    plt.title("Estimativa de π")

    plt.show()


def melhoraPi(valoresPi: list) -> None:
    """
    :param valoresPi: Lista de valores aproximados de Pi.
    """
    df = pandas.DataFrame(valoresPi, columns=['valores'])

    q1 = float(df.quantile(0.25))
    q3 = float(df.quantile(0.75))

    iqr = q3 - q1

    df2 = df[q3 + 1.5 * iqr > df['valores']]
    df3 = df2[q1 - 1.5 * iqr < df2['valores']]

    plt.scatter(range(len(df3)), df3)

    plt.xlabel("Índice")
    plt.ylabel("Valores de π")

    plt.title("Estimativa de π")

    plt.show()


main()
