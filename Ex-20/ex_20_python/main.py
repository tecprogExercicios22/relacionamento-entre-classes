from departamento import Departamento
from universidade import Universidade


def main():

    # Criamos o objeto universidade
    uni = Universidade()
    uni.setNome("UTFPR")

    # Adicionamos os departamentos à universidade
    dainf = Departamento()
    dainf.setNome("DAINF")          # Colocamos o nome do departamento
    dainf.setUniversidade(uni)      # Fornecemos a universidade afiliada
    uni.addDepartamento(dainf)      # Adicionamos o departamento à universidade

    damat = Departamento()
    damat.setNome("DAMAT")          # Colocamos o nome do departamento
    damat.setUniversidade(uni)      # Fornecemos a universidade afiliada
    uni.addDepartamento(damat)      # Adicionamos o departamento à universidade

    daeln = Departamento()
    daeln.setNome("DAELN")          # Colocamos o nome do departamento
    daeln.setUniversidade(uni)      # Fornecemos a universidade afiliada
    uni.addDepartamento(daeln)      # Adicionamos o departamento à universidade

    dafis = Departamento()
    dafis.setNome("DAFIS")          # Colocamos o nome do departamento
    dafis.setUniversidade(uni)      # Fornecemos a universidade afiliada
    uni.addDepartamento(dafis)      # Adicionamos o departamento à universidade

    # Finalmente imprimimos os departamentos associados à universidade
    uni.imprimeDepartamentos()

    return 0


if __name__ == "__main__":
    main()
