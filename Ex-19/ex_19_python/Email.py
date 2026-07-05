from Assunto import Assunto
from Mensagem import Mensagem


class Email:
    def __init__(self, assunto=None, mensagem=None):
        self.assunto = assunto if assunto is not None else Assunto()
        self.mensagem = mensagem if mensagem is not None else Mensagem()

    def setConteudoAssunto(self, assunto):
        self.assunto.setTexto(assunto)

    def addTextoMensagem(self, mensagem):
        self.mensagem.addMensagem(mensagem)

    def mostraDados(self):  # Função const por causa que não deve modificar nenhum atributo.
        print("Assunto: " + self.assunto.getTexto())
        print("Mensagem: ")
        print(self.mensagem.getMensagem())
