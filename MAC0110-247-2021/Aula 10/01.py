# Dado um número positivo N maior que 0, calcule a soma dos números de 1 a N.
n = int(input())
while n <= 0:
    n = int(input())

"""
s = 0
i = 1
while n >= i:
  s += i
  i += 1
"""

s = n * (n + 1) / 2

print(s)
