from Pessoa import Pessoa
from Universidade import Universidade
from Departamento import Departamento


def main():
    # Criamos as universidades
    princeton = Universidade()
    cambridge = Universidade()

    # Colocamos seus nomes correspondentes
    princeton.setNome("Princeton")
    cambridge.setNome("Cambridge")

    # Criamos os departamentos
    dFisicaPrinceton = Departamento("Departamento de Física", princeton)
    dMatematicaPrinceton = Departamento("Departamento de Matemática", cambridge)

    # Associamos os departamentos as universidades
    princeton.setDepartamento(dFisicaPrinceton)
    cambridge.setDepartamento(dMatematicaPrinceton)

    # Criamos as pessoas
    einstein = Pessoa()
    newton = Pessoa()

    # Prepara o objeto einstein
    einstein.setNome("Albert Einstein")
    einstein.setDataDeNascimento(13, 3, 1879)
    einstein.setDepartamento(dFisicaPrinceton)

    # Prepara o objeto newton
    newton.setNome("Issac Newton")
    newton.setDataDeNascimento(4, 1, 1643)
    newton.setDepartamento(dMatematicaPrinceton)

    # Imprime informações
    einstein.imprimeInformacao()
    newton.imprimeInformacao()
    return 0


if __name__ == "__main__":
    main()
