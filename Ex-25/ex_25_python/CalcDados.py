class CalcDados:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.operacao = '\0'

    def setOperando(self, i, valor):
        if i == 1:
            self.n1 = valor
        elif i == 2:
            self.n2 = valor
        else:
            pass

    def getOperando(self, i):
        if i == 1:
            return self.n1
        elif i == 2:
            return self.n2
        else:
            print("Operando " + str(i) + " inválido")
            exit(1)

    def setOperacao(self, operacao):
        self.operacao = operacao

    def getOperacao(self):
        return self.operacao

    def reset(self):
        self.n1 = 0
        self.n2 = 0
        self.operacao = '\0'
