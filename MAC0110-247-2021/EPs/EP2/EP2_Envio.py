from math import sqrt
from random import random

import pandas

"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Gustavo Valencio Tofolo
  NUSP : 11815267
  Turma: MAC0110-247-2021-247-2021
  Prof.: Prof. Roberto Hirata Jr.

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
  https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
  https://pandas.pydata.org/docs/index.html
"""


# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================


def main():
    pass


# E1
def mediaV(V, n):
    """
    :param V: Lista de valores numéricos;
    :param n: Número de elementos em 'V';

    :return: Média de 'V'.
    """
    s, i = 0, 0
    while i < n:
        s += V[i]
        i += 1

    return s / n


# E2
def varV(V, n):
    """
    :param V: Lista de valores numéricos;
    :param n: Número de elementos em 'V';

    :return: Variância de 'V'.
    """
    m = mediaV(V, n)
    s, i = 0, 0
    while i < n:
        s += (V[i] - m) ** 2
        i += 1

    return s / n


# E3
def PiMCM(n):
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


# E4:
def estimaPiMC(r, n):
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


# E5
def SimulaConvergenciaPi(m, r, n):
    """
    :param m: Número de simulação maiores de simulações de Monte Carlo;
    :param r: Número de simulações de Monte Carlo;
    :param n: Número de pontos aleatórios criados em cada simulação de Monte Carlo;

    :return: Médias e desvios padrões das simulações maiores.
    """
    i = 0
    medias, dps = [], []
    while i < m:
        me, v = estimaPiMC(r, n)
        medias += [me]
        dps += [sqrt(v)]
        i += 1

    return medias, dps


# E7
def leiaDados(arquivo):
    """
    :param arquivo: Nome do arquivo a ser lido;

    :return: Objeto contendo os dados do arquivo.
    """
    dados = pandas.read_csv(arquivo, sep=';')

    return dados


# E8
def calculaPi(dados):
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


# E9
def estimavaMediaPi(valoresPi):
    """
    :param valoresPi: Lista de valores aproximados de Pi;

    :return: Média e variância de 'valoresPi'.
    """
    size = len(valoresPi)
    return mediaV(valoresPi, size), varV(valoresPi, size)


# E12
def melhoraPi(valoresPi):
    """
    :param valoresPi: Lista de valores aproximados de Pi.

    :return: Média melhorada dos valores aproximados de Pi.
    """

    df = pandas.DataFrame(valoresPi, columns=['valores'])

    q1 = float(df.quantile(0.25))
    q3 = float(df.quantile(0.75))

    iqr = q3 - q1

    df2 = df[q3 + 1.5 * iqr > df['valores']]
    df3 = df2[q1 - 1.5 * iqr < df2['valores']]

    valoresPi = df3.values.tolist()

    return mediaV(valoresPi[0], len(valoresPi[0]))


# Retorne um único valor representando o pi melhorado

# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================

# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN
# ======================================================================
