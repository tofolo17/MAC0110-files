s = input("Digite uma string s: ")
i = int(input("Digite um inteiro i: "))
x = float(input("Digite um float x: "))

print(f"s = '{s}' ({type(s)})")
print(f'i = {i} ({type(i)})')
print(f'x = {x} ({type(x)})')

print(f"s + s = '{s}' + '{s}' = '{s + s}' ({type(s + s)})")
print(f"i + i = {i} + {i} = {i + i} ({type(i + i)})")
print(f"x + x = {x} + {x} = {x + x} ({type(x + x)})")

print(f"i * s = {i} * '{s}' = '{i * s}' ({type(i * s)})")
print(f"i * i = {i} * {i} = {i * i} ({type(i * i)})")
print(f"i * x = {i} * {x} = {i * x} ({type(i * x)})")

print(f"x / i = {x} / {i} = {x / i} ({type(x / i)})")
print(f"i / i = {i} / {i} = {i / i} ({type(i / i)})")
print(f"i // i = {i} // {i} = {i // i} ({type(i // i)})")

print(f"i / 2 * 3 = {i} / 2 * 3 = {i / 2 * 3} ({type(i / 2 * 3)})")
print(f"i // 2 * 3 = {i} // 2 * 3 = {i // 2 * 3} ({type(i // 2 * 3)})")
print(f"i % 3 = {i} % 3 = {i % 3} ({type(i % 3)})")
