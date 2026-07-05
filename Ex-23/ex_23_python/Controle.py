import sys

from Turma import Turma
from Aluno import Aluno


class Controle:
    def __init__(self):
        self.turma = Turma()
        self.op = 0

    def run(self):
        self.iniciarTurma()
        self.op = 0
        while True:
            # Perguntamos a operação a realizar
            self.imprimirMenu()
            self.op = int(input())
            # Verifica e executa a operação solicitada
            if self.op == 1:
                self.matricularAluno()
            elif self.op == 2:
                self.cancelarAluno()
            elif self.op == 3:
                self.imprimirRelatorio()
            elif self.op == 0:
                pass
            else:
                print("Operação Inválida :( ")
                self.op = 0
            if not self.op > 0:
                break

    def iniciarTurma(self):
        print("-> INFORMAR TURMA")
        nomeTurma = ""
        codTurma = ""
        nVagas = 0
        print("Insira <Nome Turma> <Cod. Turma> <Nro. Vagas> ")
        nomeTurma, codTurma, nVagas = input().split()
        nVagas = int(nVagas)
        # Verifica que o nro de vagas seja um nro válido
        if nVagas <= 0:
            sys.exit(1)
        # Criamos o objeto da turma com os valores fornecidos
        self.turma = Turma(nomeTurma, codTurma, nVagas)

    def matricularAluno(self):
        print("-> MATRICULAR ALUNO")
        nome = ""
        nota1 = 0
        nota2 = 0
        # Solicitamos as informações do aluno
        print("Insira <Nome Aluno> <Nota 1> <Nota 2>")
        nome, nota1, nota2 = input().split()
        nota1 = int(nota1)
        nota2 = int(nota2)
        # Criamos o objeto do aluno
        aluno = Aluno(nome, nota1, nota2)
        # Matriculamos o aluno
        self.turma.matricularAluno(aluno)

    def cancelarAluno(self):
        print("-> CANCELAR ALUNO")
        nome = ""
        # Solicitamos as informações do aluno
        print("Insira <Nome Aluno>")
        nome = input()
        # Criamos o objeto do aluno
        aluno = Aluno(nome, 0, 0)
        # Cancelamos o aluno
        self.turma.cancelarAluno(aluno)

    def imprimirRelatorio(self):
        print("-> INFORMAÇÕES DA TURMA")
        print(self.turma.gerarRelatorio())

    def imprimirMenu(self):
        print("0 - SAIR")
        print("1 - Matricular Aluno")
        print("2 - Cancelar Aluno")
        print("3 - Imprimir Relatório Turma")
