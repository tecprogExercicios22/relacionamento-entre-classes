class Item:
    def __init__(self, nome, valorUnitario, quantidade):
        self.nome = nome
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setValorUnitario(self, valorUnitario):
        self.valorUnitario = valorUnitario

    def getValorUnitario(self):
        return self.valorUnitario

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getQuantidade(self):
        return self.quantidade

    def getValorTotal(self):
        return self.valorUnitario * self.quantidade

    # Sobrecarregamos o operador == para facilitar a comparação de items
    def __eq__(self, item):
        return self.getNome() == item.getNome() and \
            self.getValorUnitario() == item.getValorUnitario() and \
            self.getQuantidade() == item.getQuantidade()
