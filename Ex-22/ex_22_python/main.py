from CarrinhoDeCompras import CarrinhoDeCompras
from Item import Item


def main():
    # Criamos o carrinho de compras
    carrinho = CarrinhoDeCompras()
    # Criamos alguns items
    notebook = Item("Notebook", 1000, 2)
    telefone = Item("Telefone", 500, 5)
    tablet = Item("Tablet", 200, 6)
    sticker = Item("Sticker", 10.5, 100)
    # Adicionamos todos os items
    carrinho.adicionarItem(notebook)
    carrinho.adicionarItem(telefone)
    carrinho.adicionarItem(tablet)
    carrinho.adicionarItem(sticker)
    # Verificamos o total
    # OBS: o std::fixed é para formatar a saída
    print("Total carrinho: " + "{:.2f}".format(carrinho.getValorTotal()))
    # Removemos alguns items
    carrinho.removerItem(notebook)
    carrinho.removerItem(tablet)
    # Verificamos o total
    print("Total carrinho: " + "{:.2f}".format(carrinho.getValorTotal()))

    return 0


if __name__ == "__main__":
    main()
