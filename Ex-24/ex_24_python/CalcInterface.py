# Inicializamos o vetor com as operacoes válidas
class CalcInterface:
    OPERACOES_VALIDAS = ['+', '-', '*', '/', 's']

    def __init__(self):
        pass

    def recebeOperando(self, i):
        print("Insira o operando " + str(i))
        operando = float(input())
        return operando

    def recebeOperacao(self):
        while True:
            print("Insira uma operacao:")
            operacao = input()
            if CalcInterface.isOperacaoValida(operacao):
                break
        return operacao

    def mostraResultado(self, resultado):
        print("Resultado: " + str(resultado))

    @staticmethod
    def isOperacaoValida(operacao):
        size = len(CalcInterface.OPERACOES_VALIDAS)
        for i in range(size):
            if CalcInterface.OPERACOES_VALIDAS[i] == operacao:
                return True
        return False
