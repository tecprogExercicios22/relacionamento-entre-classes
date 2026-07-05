class Universidade:
    # Construtora & Destrutora
    def __init__(self, nome=None, departamento=None):
        if nome is None:
            self.nome = ""
            self.departamento = None
        else:
            self.nome = nome
            self.departamento = None

    # Métodos
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento
