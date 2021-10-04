# A data da Páscoa é celebrada no primeiro domingo após a primeira lua cheia que ocorre depois do equinócio
# de primavera/outono.

# https://mundoeducacao.uol.com.br/pascoa/data-pascoa.htm
# Fórmula de Gauss: https://www.inf.ufrgs.br/~cabral/Pascoa.html


class Pascoa:
    def __init__(self, ano):
        self.ano = ano

        a = ano % 19
        b = ano // 100
        c = ano % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        ll = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * 0) // 451

        self.mes = (h + ll - 7 * m + 114) // 31
        self.dia = 1 + (h + ll - 7 * m + 114) % 31

    def get_mes(self):
        return self.mes

    def get_dia(self):
        return self.dia


pascoa = Pascoa(ano=2008)

print(pascoa.mes)
