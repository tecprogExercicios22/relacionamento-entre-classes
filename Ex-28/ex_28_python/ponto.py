class Ponto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __del__(self):
        pass

    def setPonto(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
