import random


def main():
    apostila = Apostila()
    apostila.preencher(filename='Exercícios')

    r = 'y'
    while r == 'y':
        t = input("Qual tópico deseja estudar? ('all' para qualquer um) ").capitalize()
        while t not in apostila.topicos_apostila:
            t = input('Tópico inexistente na nossa base de dados. Qual tópico deseja estudar? ')
        print(f'\n{apostila.selecionar(filtro_topico=t)}')

        r = input("Digite 'y' caso deseje gerar outro exercício: ").lower()


class Apostila:
    def __init__(self):
        self.exercicios = []
        self.topicos_apostila = ['All']

    def preencher(self, filename):
        with open(file=filename, mode='r', encoding='utf-8') as f:
            data = [line for line in f.read().splitlines() if line]

        for i in range(0, len(data), 4):
            topicos = data[i + 2].split(', ')
            exercicio = Exercicio(
                titulo=data[i],
                material=data[i + 1],
                topicos=topicos,
                enunciado=data[i + 3]
            )
            self.exercicios += [exercicio]

            for topico in topicos:
                if topico not in self.topicos_apostila:
                    self.topicos_apostila += [topico]

    def selecionar(self, filtro_topico):
        if filtro_topico != 'All':
            filtro = []
            for exercicio in self.exercicios:
                if filtro_topico in exercicio.topicos:
                    filtro.append(exercicio)
        else:
            filtro = self.exercicios

        return random.choice(filtro)


class Exercicio:
    def __init__(self, titulo, material, topicos, enunciado):
        self.titulo = titulo
        self.material = material
        self.topicos = topicos
        self.enunciado = enunciado

    def __str__(self):
        return f'{self.titulo}\n{self.material}\n{self.topicos}\n{self.enunciado}\n'


main()
