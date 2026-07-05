class Familia:
    def __init__(self, sobrenomeF=""):
        self.pPrincipal = None
        self.pConjuge = None
        self.listaFilhos = []
        self.sobrenome = sobrenomeF

    def getSobrenome(self):
        return self.sobrenome

    def listarArvoreFamiliar(self):

        print("Familia " + self.sobrenome)
        print("Principal: ", end="")
        if self.pPrincipal is not None:
            print(self.pPrincipal.getNomeCompleto())
        else:
            print("Não definido")

        print("Conjuge: ", end="")
        if self.pConjuge is not None:
            print(self.pConjuge.getNomeCompleto())
        else:
            print("Não definido")

        print("Filhos: ", end="")
        if len(self.listaFilhos) > 0:
            print()
            for i in range(len(self.listaFilhos)):
                print(" - " + self.listaFilhos[i].getNomeCompleto())
        else:
            print("A familia não possui filhos!")

    def adicionarFilho(self, pFilho):
        if pFilho is None:
            print("Ponteiro para filho NULL")
            return
        self.listaFilhos.append(pFilho)

        pFilho.setFamilia(self)
        pFilho.setMae(self.pPrincipal)
        pFilho.setPai(self.pConjuge)

        if self.pPrincipal:
            self.pPrincipal.adicionarFilho(pFilho)

        if self.pConjuge:
            self.pConjuge.adicionarFilho(pFilho)

    def setPrincipal(self, p):
        self.pPrincipal = p
        p.setFamilia(self)

    def setConjuge(self, p):
        self.pConjuge = p
        p.setFamilia(self)
