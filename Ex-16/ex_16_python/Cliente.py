class Cliente:
    # Constante com o nro máximo de contas
    N_MAX_CONTAS = 3

    # Construtora & Destrutora
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.nContas = 0
        # Cria vetor para as contas
        self.contas = [None] * Cliente.N_MAX_CONTAS
        # Inicializamos todas as posicoes
        for i in range(Cliente.N_MAX_CONTAS):
            self.contas[i] = None

    def adicionarConta(self, conta):
        if self.nContas < Cliente.N_MAX_CONTAS:
            # Adiciona nova conta
            self.contas[self.nContas] = conta
            # Aumenta nro de contas
            self.nContas += 1

    # Métodos requeridos
    def gerarRelatorio(self):
        # Cria o string
        ss = self.nome + " | " + self.cpf + " | N. Contas: " + str(self.nContas)

        for i in range(self.nContas):
            ss += " | Saldo Conta[" + str(i) + "]<" + str(self.contas[i].getNumero()) + ">: " + str(self.contas[i].getSaldo())

        return ss

    def aplicarRecursos(self, valor, iConta=0):
        # Verifica que a posicao da conta seja valida
        if self.nContas > iConta:
            self.contas[iConta].depositar(valor)
