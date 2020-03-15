class stateItself:

    def __init__(self, listado, nombre):
        self.listado = listado
        self.nombre = nombre


class automataDefinition:

    def __init__(self, estados):
        self.estadoNombre = estados[0].nombre
        self.lstEstados = estados
        self.estado=estados[0]

    def transicion(self, numero):
        estadoActual = None
        for x in range(0,len(self.lstEstados)):
            if self.lstEstados[x].nombre == self.estadoNombre:
                estadoActual = self.lstEstados[x]
                break
        if estadoActual != None:
            
            for camino in estadoActual.listado:
                if camino[0]==numero:
                    self.estadoNombre=camino[1]
                    print(self.estadoNombre)