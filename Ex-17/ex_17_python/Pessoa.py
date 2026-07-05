import time

from Universidade import Universidade


class Pessoa:
    # Construtora: inicializamos os atributos.
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.diaN = 0
        self.mesN = 0
        self.anoN = 0
        self.universidade = None

    # Calcula a idade utilizando diaN, mesN e anoN; logo guarda o valor
    # no attributo idade.
    def caculaIdade(self):
        # Obtem a data atual utilizando a biblioteca "ctime"
        tms = time.localtime(time.time())

        # Calcula a idade
        self.idade = tms.tm_year - self.anoN

        # Verifica se a data do aniversário já passou, para ajustar a idade.
        if self.mesN > tms.tm_mon or (self.mesN == tms.tm_mon and self.diaN < tms.tm_mday):
            self.idade -= 1

    # Retorna a idade da pessoa.
    def getIdade(self):
        return self.idade

    # Atualiza o nome da pessoa.
    def setNome(self, nome):
        self.nome = nome

    # Retorna o nome da pessoa.
    def getNome(self):
        return self.nome

    # Atualiza a data de nacimento da pessoa.
    def setDataDeNascimento(self, diaN, mesN, anoN):
        # ATENÇÃO:
        # Utilizando "self." nos referimos ao atributo privado do objeto,
        # não aos parametros da função
        self.diaN = diaN
        self.mesN = mesN
        self.anoN = anoN
        # Calculamos a idade sempre que a data de nascimento é atualizada
        self.caculaIdade()

    def setUniversidade(self, universidade):
        self.universidade = universidade

    def getUniversidade(self):
        return self.universidade

    def imprimeInformacao(self):
        nUni = ""
        # Verificamos se a pessoa está associada a uma universidade
        if self.universidade:
            nUni = self.universidade.getNome()

        print(self.nome + " | Idade: " + str(self.getIdade()) + " | Universidade: " + nUni)
