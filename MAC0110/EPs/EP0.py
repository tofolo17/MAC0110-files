def main():
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))

    print(f"MDC({a},{b}) = {mdc(a, b)}")


# Algoritmo de euclides
def mdc(a, b):
    if a == 0:
        return b

    return mdc(b % a, a)


main()
"""
d = a
while not(a % d == 0 and b % d == 0):
    d -= d

print(d)
"""
