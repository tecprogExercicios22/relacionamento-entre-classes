from poligono import Poligono
from ponto import Ponto


class Principal:
    def __init__(self):
        self.polig = Poligono()
        self.exec()

    def __del__(self):
        pass

    def exec(self):
        opcao = 1
        while opcao != 0:
            print("\n=========================================")
            print("1 - Incluir ponto no poligono\n2 - Remover ponto do Poligono\n3 - Imprimir perimetro do poligono\n4 - Imprimir todos os prontos\n0 - Sair")
            print("=========================================\nSelecione uma opçao: ", end="")
            opcao = int(input())
            print("=========================================")
            if opcao == 1:
                self.lerPonto()
            elif opcao == 2:
                self.removerPonto()
            elif opcao == 3:
                self.imprimirPerimetro()
            elif opcao == 4:
                self.polig.imprimirTodosPontos()
            else:
                pass

    def lerPonto(self):
        print("\nDigite a coordenada do vertice no formato(x.x, y.y) :", end="")
        entrada = input()
        entrada = entrada.strip().lstrip("(").rstrip(")")
        partes = entrada.split(",")
        x = float(partes[0])
        y = float(partes[1])

        tmp = Ponto()
        tmp.setPonto(x, y)

        self.polig.setVertice(tmp)

    def imprimirPerimetro(self):
        self.polig.imprimirPerimetro()

    def removerPonto(self):
        self.polig.imprimirTodosPontos()
        print("\nQual ponto deseja remover? ", end="")

        x = int(input())

        self.polig.removerPonto(self.polig[x])
