class Mensagem:
    def __init__(self):
        self.texto = ""

    def addMensagem(self, texto):
        self.texto = texto

    def getMensagem(self):
        return self.texto
