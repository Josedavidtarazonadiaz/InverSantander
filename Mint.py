class Night:
    def __init__(self, Dato):
        self.Indat = Dato
        self.SigEn1 = None  # Hijo DERECHO (Valores mayores)
        self.Sigen2 = None  # Hijo IZQUIERDO (Valores menores)
        self.Father = None

    def ONd(self):
        return self.Indat

class Pencil:
    def __init__(self):
        self.rz = None

    def InsertNod(self, Dat):
        NuevNOD = Night(Dat)
        if self.rz is None:
            self.rz = NuevNOD
            return
        Actua = self.rz
        while True:
            if Dat < Actua.Indat:
                if Actua.Sigen2 is None:  
                    Actua.Sigen2 = NuevNOD
                    NuevNOD.Father = Actua
                    return
                Actua = Actua.Sigen2
            elif Dat > Actua.Indat:
                if Actua.SigEn1 is None:  
                    Actua.SigEn1 = NuevNOD
                    NuevNOD.Father = Actua
                    return
                Actua = Actua.SigEn1
            else:
                return

    def Inord(self, Nod, Rest=None):
        if Rest is None: Rest = []
        if Nod is None: return Rest
        
        self.Inord(Nod.Sigen2, Rest)
        Rest.append(Nod.Indat)
        self.Inord(Nod.SigEn1, Rest)

        return Rest

    def LNE(self, Nota1, Nota2):
        limitInf = min(Nota1, Nota2)
        limitSup = max(Nota1, Nota2)
        resut = []

        def BusqRango(Nod):
            if Nod is None:
                return

            if limitInf < Nod.Indat:
                BusqRango(Nod.Sigen2)

            if limitInf <= Nod.Indat <= limitSup:
                resut.append(Nod.Indat)

            if Nod.Indat < limitSup:
                BusqRango(Nod.SigEn1)
        
        BusqRango(self.rz)
        return resut

    def CalcularPromedio(self):
        def CalSumaPeso(Nod):
            if Nod is None:
                return 0, 0

            SumaIzq, PesoIzq = CalSumaPeso(Nod.Sigen2)
            SumaDer, PesoDer = CalSumaPeso(Nod.SigEn1)

            SumaTot = SumaIzq + SumaDer + Nod.Indat
            PesoTot = PesoIzq + PesoDer + 1
            
            return SumaTot, PesoTot

        if self.rz is None:
            return 0.0

        SumaTot, PesoTot = CalSumaPeso(self.rz)

        if PesoTot == 0:
            return 0.0

        return SumaTot / PesoTot

    def _ObtAlt(self, Nod):
        if Nod is None:
            return -1
        
        AltIzq = self._ObtAlt(Nod.Sigen2)
        AltDer = self._ObtAlt(Nod.SigEn1)

        return 1 + max(AltIzq, AltDer)

    def IdentificarFB(self, Nod):
        if Nod is None:
            return 0 

        AltDer = self._ObtAlt(Nod.SigEn1)
        AltIzq = self._ObtAlt(Nod.Sigen2)
        
        return AltDer - AltIzq
    
    def ListarTodosFB(self):
        FBdict = {}
        
        def RecorrerYCalcular(Nod):
            if Nod is None:
                return

            FBdict[Nod.Indat] = self.IdentificarFB(Nod)

            RecorrerYCalcular(Nod.Sigen2)
            RecorrerYCalcular(Nod.SigEn1)

        RecorrerYCalcular(self.rz)
        return FBdict