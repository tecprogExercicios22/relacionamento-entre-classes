from CalcDados import CalcDados
from CalcInterface import CalcInterface
from CalcControle import CalcControle


class Calculadora:
    # cria os componentes e os vínculos (via lista de inicialização)
    def __init__(self):
        self.dados = CalcDados()
        self.interface = CalcInterface()
        self.controle = CalcControle(self.interface, self.dados)

    def funcionar(self):
        self.interface.mostraBoasVindas()
        self.dados.reset()
        self.controle.executar()
