from Triangulo import Triangulo


class Principal:
    def __init__(self):
        self.triang = Triangulo()
        self.exec()

    def __del__(self):
        pass

    def exec(self):
        x, y = 0, 0

        print("Criando um triangulo... \nDigite a coordenada do primeiro vertice no formato (x.x,y.y): ", end="")
        x, y = self.lerCoordenada()
        self.triang.setVertice1(x, y)

        print("Digite a coordenada do segundo vertice no formato (x.x,y.y): ", end="")
        x, y = self.lerCoordenada()
        self.triang.setVertice2(x, y)

        print("Digite a coordenada do terceiro vertice no formato (x.x,y.y): ", end="")
        x, y = self.lerCoordenada()
        self.triang.setVertice3(x, y)

        self.triang.imprimirPerimetro()

    def lerCoordenada(self):
        entrada = input().strip().lstrip("(").rstrip(")")
        partes = entrada.split(",")
        return float(partes[0]), float(partes[1])
