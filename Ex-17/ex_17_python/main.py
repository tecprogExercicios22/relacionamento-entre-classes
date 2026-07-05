from Universidade import Universidade
from Pessoa import Pessoa


def main():
    # Criamos as universidades
    princeton, cambridge = Universidade(), Universidade()

    # Colocamos seus nomes correspondentes
    princeton.setNome("Princeton")
    cambridge.setNome("Cambridge")

    # Criamos as pessoas
    einstein, newton = Pessoa(), Pessoa()

    # Prepara o objeto einstein
    einstein.setNome("Albert Einstein")
    einstein.setDataDeNascimento(13, 3, 1879)
    einstein.setUniversidade(princeton)

    # Prepara o objeto newton
    newton.setNome("Issac Newton")
    newton.setDataDeNascimento(4, 1, 1643)
    newton.setUniversidade(cambridge)

    # Imprime informações
    einstein.imprimeInformacao()
    newton.imprimeInformacao()
    return 0


if __name__ == "__main__":
    main()
