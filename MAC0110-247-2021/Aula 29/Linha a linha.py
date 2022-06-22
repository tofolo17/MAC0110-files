filename = "Queijo"

with open(file=filename, mode='r', encoding='utf-8') as f:
    text = f.read()

linhas = text.split('\n')
for i in range(len(linhas)):
    linha = linhas[i]

    print(f'{i + 1}. {linha}')
