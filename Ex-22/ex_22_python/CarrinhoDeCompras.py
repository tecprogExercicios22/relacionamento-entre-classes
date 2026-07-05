from Item import Item


class CarrinhoDeCompras:
    def __init__(self):
        self.items = []

    def adicionarItem(self, i):
        self.items.append(i)

    def removerItem(self, i):
        self.items.remove(i)

    def getValorTotal(self):
        total = 0.0
        it = 0
        while it != len(self.items):
            total += self.items[it].getValorTotal()
            it += 1
        return total
