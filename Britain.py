class Mangost:
    def __init__(self, Idat):
        self.Dat = Idat
        self.NodoEn = None
        self.firsthj = None 
        self.fath = None

    def ON_D(self):
        return self.Dat

    def ON_S(self):
        return self.NodoEn

    def Agrhjs(self, Nhij):
        Nhij.fath = self

        if self.firsthj is None:
            self.firsthj = Nhij
        else:
            Utim = self.firsthj
            while Utim.NodoEn is not None:
                Utim = Utim.NodoEn

            Utim.NodoEn = Nhij

    def EminHJS(self, NodHijEM):
        if self.firsthj is NodHijEM:
            self.firsthj = NodHijEM.NodoEn
            NodHijEM.fath = None
            NodHijEM.NodoEn = None
            return True

        noDActua = self.firsthj

        while noDActua is not None and noDActua.NodoEn is not NodHijEM:
            noDActua = noDActua.NodoEn

        if noDActua is not None:
            noDActua.NodoEn = NodHijEM.NodoEn
            NodHijEM.fath = None
            NodHijEM.NodoEn = None
            return True

        return False

    def ObtnHjs(self):
        IstaHijos = []
        nodACT = self.firsthj

        while nodACT is not None:
            IstaHijos.append(nodACT)
            nodACT = nodACT.NodoEn

        return IstaHijos

    def EsHj(self):
        return self.firsthj is None
    
    def EsRM(self):
        return self.firsthj is not None

class Mong: 
    def __init__(self, dato_raiz):
        self.raiz = Mangost(dato_raiz)
        
    def obtenerNivel(self, dato):
        def buscar_nivel(nodo_actual, nivel):
            if nodo_actual is None:
                return -1
            if nodo_actual.Dat == dato:
                return nivel
            
            for hijo in nodo_actual.ObtnHjs():
                nivel_encontrado = buscar_nivel(hijo, nivel + 1)
                if nivel_encontrado != -1:
                    return nivel_encontrado
            return -1

        return buscar_nivel(self.raiz, 0)
    
    def obtenerAltura(self):
        def calcular_altura(nodo):
            if nodo.firsthj is None: 
                return 0
            
            max_altura_hijos = 0
            for hijo in nodo.ObtnHjs():
                max_altura_hijos = max(max_altura_hijos, calcular_altura(hijo))
            
            return 1 + max_altura_hijos

        if not self.raiz:
            return -1
        return calcular_altura(self.raiz)

    def obtenerPeso(self):
        def contar_nodos(nodo):
            if nodo is None:
                return 0
            
            conteo = 1
            for hijo in nodo.ObtnHjs():
                conteo += contar_nodos(hijo)
            return conteo

        return contar_nodos(self.raiz)

    def obtenerGrado(self, nodo_o_dato):
        if isinstance(nodo_o_dato, Mangost):
            return len(nodo_o_dato.ObtnHjs())
        
        return 0

    def preOrden(self, nodo, resultados=None):
        if resultados is None:
            resultados = []
        if nodo is None:
            return resultados

        resultados.append(nodo.Dat)

        for hijo in nodo.ObtnHjs():
            self.preOrden(hijo, resultados)
            
        return resultados

    def postOrden(self, nodo, resultados=None):
        if resultados is None:
            resultados = []
        if nodo is None:
            return resultados

        for hijo in nodo.ObtnHjs():
            self.postOrden(hijo, resultados)
        
        resultados.append(nodo.Dat)

        return resultados
    
    def inOrden(self, nodo, resultados=None):
        if resultados is None:
            resultados = []
        if nodo is None:
            return resultados

        hijos = nodo.ObtnHjs()
        
        if hijos:
            self.inOrden(hijos[0], resultados)
        
        resultados.append(nodo.Dat)
        
        for i in range(1, len(hijos)):
            self.inOrden(hijos[i], resultados)

        return resultados
