class NoQ:
    def __init__(self,ato):
        self.Idat = ato
        self.csig = None
        self.Prant = None

    def ODat(self):
        return self.Idat

    def OSig(self):
        return self.csig.Idat

    def OAnt(self):
        return self.Prant.Idat

    def EstSig(self,NNodq):
        self.csig = NNodq

    def EstAnt(self,Nnq):
        self.Prant = Nnq

class Nictname:

    def __init__(self,capta):
        self.Capt = capta
        self.top = None
        self.bot = None
        self.tam = 0

    def enqueQ(self,dat):
        if self.ESTllen():
            print()
            return
        Nnodoq = NoQ(dat)
        if self.Ivacs():
            self.top = Nnodoq
            self.bot = Nnodoq
        else:
            self.bot.csig = Nnodoq
            Nnodoq.Prant = self.bot
            self.bot = Nnodoq
        self.tam += 1
        print

    def DeqQ(self,dat):
        if self.Ivacs():
            print()
            return None

        Datem = self.top.Idat

        if self.top == self.bot:
            self.top = None
            self.bot = None
        else:
            self.top = self.top.csig
            self.bot.Prant = None

        self.tam -= 1
        return Datem

    def frentENQ(self):
        if self.Ivacs():
            return None
        return self.top.Idat

    def UltimENQ(self):
        if self.Ivacs():
            return None
        return self.bot.Idat

    def ESTllen(self):
        return self.tam == self.Capt

    def Record(self):
        if self.Ivacs():
            print()
            return

        Actt = self.top
        print()
        while Actt:
            print()
            Actt = Actt.csig
        print()

    def Ivacs(self):
        return self.top is None



























































































