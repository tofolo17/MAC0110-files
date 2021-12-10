def main():
    apostila = Apostila()
    print(apostila.exercicios)

    apostila.preencher(filename='Exercícios')
    print(apostila.exercicios)


class Apostila:
    def __init__(self):
        self.exercicios = []

    def preencher(self, filename):
        for i in range(3):
            exercicio = Exercicio(i, i, i, filename)
            self.exercicios += [exercicio]

    def selecionar(self, topico, lock):
        return self.exercicios[0], topico, lock


class Exercicio:
    def __init__(self, titulo, material, topico, enunciado):
        self.titulo = titulo
        self.material = material
        self.topico = topico
        self.enunciado = enunciado

    def __str__(self):
        return f'{self.titulo}'

    def __repr__(self):
        return f'{self.titulo}'


main()
