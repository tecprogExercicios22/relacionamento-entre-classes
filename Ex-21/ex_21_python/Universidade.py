import sys


class Universidade:
    MAX_DEPARTAMENTOS = 50

    # Construtora & Destrutora
    def __init__(self):
        self.nome = ""
        self.lDepartamentos = []
        self.nDepartamentos = 0

    # Métodos
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def addDepartamento(self, departamento):
        if self.nDepartamentos < self.MAX_DEPARTAMENTOS:
            self.lDepartamentos.insert(0, departamento)
            self.nDepartamentos += 1
        else:
            print("Máximo 50 departamentos", file=sys.stderr)
            sys.exit(1)

    def imprimeDepartamentos(self):
        print("Departamentos: ")
        for departamento in self.lDepartamentos:
            print("\t -> " + departamento.getNome())
