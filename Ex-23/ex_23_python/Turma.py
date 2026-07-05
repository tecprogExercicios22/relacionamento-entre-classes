from Aluno import Aluno


class Turma:
    NOTA_MIN_APROVADO = 60
    NOTA_MIN_RECUPARACAO = 20

    def __init__(self, nomeTurma="", codTurma="", nVagas=0):
        self.nomeTurma = nomeTurma
        self.codTurma = codTurma
        self.nVagas = nVagas
        self.nVagasOcupadas = 0
        self.alunos = []

    def matricularAluno(self, aluno):
        if self.nVagasOcupadas < self.nVagas:
            self.alunos.append(aluno)
            self.nVagasOcupadas += 1

    def cancelarAluno(self, aluno):
        # Buscamos o aluno
        it = 0
        existe = False
        while not existe and it != len(self.alunos):
            if self.alunos[it] == aluno:
                existe = True
            it += 1
        # Removemos o aluno caso ele exista
        if existe:
            self.alunos.remove(aluno)
            self.nVagasOcupadas -= 1

    def getMediaTurma(self):
        it = 0
        # Somamos todas as medias e divimos pelo nro de alunos
        # para tirar a media das medias.
        media = 0
        while it != len(self.alunos):
            media += self.alunos[it].getMedia()
            it += 1

        return media / self.nVagasOcupadas

    def getNroAlunosAprovados(self):
        it = 0

        nAlunos = 0
        while it != len(self.alunos):
            if self.alunos[it].getMedia() >= Turma.NOTA_MIN_APROVADO:
                nAlunos += 1
            it += 1

        return nAlunos

    def getNroAlunosParaFinal(self):
        it = 0

        nAlunos = 0
        while it != len(self.alunos):
            if (self.alunos[it].getMedia() < Turma.NOTA_MIN_APROVADO and
                    self.alunos[it].getMedia() >= Turma.NOTA_MIN_RECUPARACAO):
                nAlunos += 1
            it += 1

        return nAlunos

    def getNroAlunosReprovados(self):
        it = 0

        nAlunos = 0
        while it != len(self.alunos):
            if self.alunos[it].getMedia() < Turma.NOTA_MIN_RECUPARACAO:
                nAlunos += 1
            it += 1

        return nAlunos

    def getNomeAlunosAbaixoMedia(self):
        it = 0

        alunos = ""
        mediaTurma = self.getMediaTurma()
        while it != len(self.alunos):
            if self.alunos[it].getMedia() < mediaTurma:
                alunos += self.alunos[it].getNome() + " | "
            it += 1

        return alunos

    def gerarRelatorio(self):
        ss = ""
        ss += "Média da Turma: " + str(self.getMediaTurma()) + "\n"
        ss += "Número alunos (Total | Aprovados | P/Final | Reprovados): " + str(self.nVagasOcupadas) + " | " + str(self.getNroAlunosAprovados()) + " | " + str(self.getNroAlunosParaFinal()) + " | " + str(self.getNroAlunosReprovados()) + "\n"
        ss += "Alunos abaixo da média: " + self.getNomeAlunosAbaixoMedia() + "\n"
        return ss
