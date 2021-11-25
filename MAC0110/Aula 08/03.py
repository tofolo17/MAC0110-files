# Data 01
d1 = int(input())
m1 = int(input())
a1 = int(input())

# Data 02
d2 = int(input())
m2 = int(input())
a2 = int(input())

# Comparação
if a1 > a2 or (a1 == a2 and m1 > m2) or (a1 == a2 and m1 == m2 and d1 > d2):
    # Pela álgebra booleana, a1>a2 or (a1==a2 and (m1>m2 or (m1==m2 and d1>d2))):
    print("Data 01 maior que data 02.")
elif a1 == a2 and m1 == m2 and d1 == d2:
    print('Data 01 igual data 02.')
else:
    print("Data 02 maior que data 01.")
