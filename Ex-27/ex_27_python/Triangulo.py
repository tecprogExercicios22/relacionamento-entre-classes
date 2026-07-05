import math

from Ponto import Ponto


class Triangulo:
    def __init__(self):
        self.vertice1 = Ponto()
        self.vertice2 = Ponto()
        self.vertice3 = Ponto()

    def __del__(self):
        del self.vertice1
        del self.vertice2
        del self.vertice3

    def setVertice1(self, x, y):
        self.vertice1.setPonto(x, y)

    def setVertice2(self, x, y):
        self.vertice2.setPonto(x, y)

    def setVertice3(self, x, y):
        self.vertice3.setPonto(x, y)

    def getPVertice1(self):
        return self.vertice1

    def getPVertice2(self):
        return self.vertice2

    def getPVertice3(self):
        return self.vertice3

    # Calcula e imprime o perimetro do triangulo
    def imprimirPerimetro(self):
        perimetro = 0

        if not self.testeTriangulo():
            print("Os vértices não formam um triangulo, pois são colineares.")
            return

        perimetro += self.calcDist(self.vertice1, self.vertice2)
        perimetro += self.calcDist(self.vertice2, self.vertice3)
        perimetro += self.calcDist(self.vertice1, self.vertice3)

        print("O perimetro do triangulo é " + str(perimetro))

    # Testa se os vertices foram um triangulo
    def testeTriangulo(self):
        if self.vertice1.getX() == self.vertice2.getX() and self.vertice1.getX() == self.vertice3.getX():
            return False
        if self.vertice1.getY() == self.vertice2.getY() and self.vertice1.getY() == self.vertice3.getY():
            return False
        return True

    # Calcula a distancia entre dois pontos
    def calcDist(self, p1, p2):
        return math.sqrt((p1.getX() - p2.getX()) * (p1.getX() - p2.getX()) + (p1.getY() - p2.getY()) * (p1.getY() - p2.getY()))
