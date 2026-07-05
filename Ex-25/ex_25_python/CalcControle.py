from CalcDados import CalcDados
from CalcInterface import CalcInterface


class CalcControle:
    def __init__(self, calcInterface=None, calcDados=None):
        if calcInterface is None and calcDados is None:
            self.inteface = CalcInterface()
            self.dados = CalcDados()
        else:
            self.inteface = calcInterface
            self.dados = calcDados

    def executar(self):
        # Carregamos os dados
        self.dados.setOperando(1, self.inteface.recebeOperando(1))
        # Loop da calculadora
        while self.dados.getOperacao() != 's':
            self.dados.setOperando(2, self.inteface.recebeOperando(2))
            self.dados.setOperacao(self.inteface.recebeOperacao())

            # valida operacao
            if self.dados.getOperacao() != 's':
                # Executamos a operacao
                resultado = self.operar(self.dados.getOperando(1), self.dados.getOperando(2), self.dados.getOperacao())
                # Mostramos o resultado
                self.inteface.mostraResultado(resultado)
                # Armazena resultado como primeiro operando e volta para o segundo passo
                self.dados.setOperando(1, resultado)
            else:
                # Caso operação == s, finaliza a calculadora
                print("Calculadora Finalizada!", end="")
                exit(0)

    def operar(self, n1, n2, operacao):
        if operacao == '*':
            return n1 * n2
        elif operacao == '/':
            return n1 / n2
        elif operacao == '-':
            return n1 - n2
        elif operacao == '+':
            return n1 + n2
        elif operacao == 's':
            return 0
        else:
            print("Operação " + operacao + " inválida")
            exit(1)
