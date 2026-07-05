class Departamento:
    def __init__(self, nome=None, universidade=None):
        if nome is None:
            self.nome = ""
            self.universidade = None
        else:
            self.nome = nome
            self.universidade = universidade

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setUniversidade(self, universidade):
        self.universidade = universidade

    def getUniversidade(self):
        return self.universidade
