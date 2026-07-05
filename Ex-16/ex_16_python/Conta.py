class Conta:
    # Construtora & Destrutora
    def __init__(self, nroConta):
        self.nroConta = nroConta
        self.saldo = 0.0
        self.titular = None

    # Getters & Setters
    def getSaldo(self):
        return self.saldo

    def getNumero(self):
        return self.nroConta

    def getTitular(self):
        return self.titular

    def setTitular(self, cliente):
        self.titular = cliente

    # Métodos requeridos
    def sacar(self, valor):
        # Verifica que o valor seja positivo
        if valor > 0:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        # Verifica que o valor seja positivo
        if valor > 0:
            self.saldo += valor
            return True
        return False
