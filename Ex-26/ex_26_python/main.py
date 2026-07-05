from Pessoa import Pessoa
from Familia import Familia


def main():
    filho1 = Pessoa("Pedro Almeida")
    filho2 = Pessoa("Lucas Augusto")
    pai = Pessoa("Carlão Souza")
    mae = Pessoa("Maria Giovanni")

    jhonson = Familia("Jhonson")
    jhonson.setConjuge(pai)
    jhonson.setPrincipal(mae)
    jhonson.adicionarFilho(filho1)
    jhonson.adicionarFilho(filho2)

    jhonson.listarArvoreFamiliar()

    pai.listarFilhos()

    return 0


if __name__ == "__main__":
    main()
