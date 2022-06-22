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
  Turma: 247-2021
  Prof.: Roberto Hirata Junior

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  realpython.com/python-f-strings/
  https://docs.python.org/3/library/math.html
"""

import math

r2 = float(input("Digite o valor do maior raio: "))
r1 = float(input("Digite o valor do menor raio: "))

xp = float(input("Digite o valor da coordenada x do ponto p: "))
yp = float(input("Digite o valor da coordenada y do ponto p: "))

d = math.sqrt(xp * xp + yp * yp)

if d > r2:
    pontuacao = 0
elif d > r1:
    pontuacao = 20
else:
    pontuacao = 50

print(f"Sua pontuacao foi: {pontuacao}")
