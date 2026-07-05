import math
import sys

from ponto import Ponto


class Poligono:
    def __init__(self):
        self.pontos = []

    def __del__(self):
        for i in range(self.getQuantidadePontos()):
            self.pontos[i] = None
        self.pontos.clear()

    def setVertice(self, pPonto):
        if pPonto is None:
            print("Ponteiro NULL ao incluir novo vertice em Poligono")
            sys.exit(1)

        self.pontos.append(pPonto)

    # Calcula e imprime o perimetro do Poligono
    def imprimirPerimetro(self):
        perimetro = 0

        # Soma todas as distancias entre os pontos
        for i in range(self.getQuantidadePontos() - 1):
            perimetro += self.calcDist(self.pontos[i], self.pontos[i + 1])
        # Falta somar a distancia do ultimo ponto para o primeiro
        if self.getQuantidadePontos() - 1 > 1:
            perimetro += self.calcDist(self.pontos[self.getQuantidadePontos() - 1], self.pontos[0])

        print("O perimetro do Poligono é " + str(perimetro))

    # Acessa o vetor retornando o Ponto correspondente ao indice i do vetor
    def __getitem__(self, i):
        if i < 0 or i >= self.getQuantidadePontos():
            print("Vector out of range.")
            sys.exit(8)

        return self.pontos[i]

    # Pega a quantiade de pontos
    def getQuantidadePontos(self):
        return len(self.pontos)

    # Calcula a distancia entre dois pontos
    def calcDist(self, p1, p2):
        return math.sqrt((p1.getX() - p2.getX()) * (p1.getX() - p2.getX()) + (p1.getY() - p2.getY()) * (p1.getY() - p2.getY()))

    # Remover ponto do poligono
    def removerPonto(self, pPonto):
        for tmp in self.pontos:
            if tmp == pPonto:
                if pPonto is not None:
                    self.pontos.remove(pPonto)
                return

    # Imprime todos os pontos e seu indice
    def imprimirTodosPontos(self):
        print("Imprimindo pontos poligono: \nindice - (x,y)")

        if self.getQuantidadePontos() < 1:
            print("Nao ha pontos nesse poligono!")
            return

        for i in range(self.getQuantidadePontos()):
            tmp = self.pontos[i]
            if tmp:
                print(str(i) + " - (" + str(tmp.getX()) + "," + str(tmp.getY()) + ")")
            else:
                print(str(i) + " - sem coordenadas")
