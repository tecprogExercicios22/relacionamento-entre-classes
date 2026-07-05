class Pessoa:
    def __init__(self, n="", pMae=None, pPai=None):
        self.nome = n
        self.mae = pMae
        self.pai = pPai
        self.pFamilia = None
        self.listaFilhos = []

    def getNome(self):
        return self.nome

    def getNomeCompleto(self):
        nomeCompleto = self.nome

        if self.pFamilia is not None:
            nomeCompleto += " "
            nomeCompleto += self.pFamilia.getSobrenome()

        return nomeCompleto

    def setNome(self, nome):
        self.nome = nome

    def imprimeNomeCompleto(self):
        if self.pFamilia:
            print(self.nome + " " + self.pFamilia.getSobrenome())
        else:
            print(self.nome)

    def setFamilia(self, pFm):
        self.pFamilia = pFm

    def setMae(self, pMae):
        if pMae is None:
            print("Ponteiro para mae NULL")
            return
        self.mae = pMae

    def setPai(self, pPai):
        if pPai is None:
            print("Ponteiro para pai NULL")
            return
        self.pai = pPai

    def adicionarFilho(self, pFilho):
        if pFilho is None:
            print("Ponteiro para filho NULL")
            return
        self.listaFilhos.append(pFilho)

    def listarFilhos(self):
        if len(self.listaFilhos) < 1:
            print(self.getNomeCompleto() + " não possui filhos!")
            return

        print("Filhos de " + self.getNomeCompleto() + ":")

        for i in range(len(self.listaFilhos)):
            print(" - " + self.listaFilhos[i].getNomeCompleto())
