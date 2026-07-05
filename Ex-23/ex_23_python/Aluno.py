class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota1(self):
        return self.nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2

    def getMedia(self):
        return (self.getNota1() + self.getNota2()) // 2

    # Sobrecarregamos o operador == para facilitar a comparação entre alunos
    def __eq__(self, aluno):
        return self.getNome() == aluno.getNome()
