#Practica 4 Ricardo Alberto Machorro Vences
from openpyxl import load_workbook


primerEstadoInicial=""
listaEstadosFinalesIniciales=[]
listaEstadosIniciales=[]
listaEstadosDesechadosConvexo=set()
listaEstadosAutomataConvexo=set()
listaEstadosFinalesConvexo=set()

def verprimerEstadoInicial(posibleprimerEstadoInicial):
    if(posibleprimerEstadoInicial[0]=="→"):
        return True
    else:
        return False

def verEstadosFinal(posibleEstadoFinal):
    if(posibleEstadoFinal[0]=="*"):
        return True
    else:
        return False

def estadosConvexo(estadoInicial,listaEstadosFinales,listaEstados,sheetExcel):
    final=False
    listaEstVerificados=set()
    listaEstVerificados.add(estadoInicial)
    listaEstadosEsperaAnt=set()
    listaEstadosEsperaAnt.add(estadoInicial)
    listaEstadosEsperaNuevos=set()
    while(final==False):
        for row in sheetExcel.iter_rows(min_row=2):
            if(row[0].value!=None):
                valorCelda=""
                if(verprimerEstadoInicial(row[0].value) or verEstadosFinal(row[0].value)):
                    valorCelda=row[0].value[1:len(row[0].value)]
                else:
                    valorCelda=row[0].value
                if(valorCelda in listaEstadosEsperaAnt):
                    for i in range(1,sheetExcel.max_column):
                        listaEstVerificados.add(row[i].value)
                        listaEstadosEsperaNuevos.add(row[i].value)
            else:
                break
                break      
        listaEstadosEsperaNuevos=listaEstadosEsperaNuevos-listaEstadosEsperaAnt
        if (len(listaEstadosEsperaNuevos)==0):
            final=True
        else:
            listaEstadosEsperaAnt=listaEstadosEsperaNuevos
            listaEstadosEsperaNuevos.clear()
    print(listaEstVerificados)

def estadosConvexosNuevo(estadoInicial,listaEstadosFinales,listaEstados,sheetExcel):
    final=False
    listaEstadosVerificados=set()
    listaEstadosBusTerminada=set()
    listaEstadosVerificados.add(estadoInicial)
    listaEstadosBusPendienteAhora=set()
    listaEstadosBusPendienteAhora.add(estadoInicial)
    listaEstadosBusPendienteNuevos=set()
    while(final==False):
        for row in sheetExcel.iter_rows(min_row=2):
            if(row[0].value!=None):
                valorCelda=""
            if(verprimerEstadoInicial(row[0].value) or verEstadosFinal(row[0].value)):
                valorCelda=row[0].value[1:len(row[0].value)]
            else:
                valorCelda=row[0].value
            if(valorCelda in listaEstadosBusPendienteAhora):
                for i in range(1,sheetExcel.max_column):
                     listaEstadosVerificados.add(row[i].value)
                     listaEstadosBusPendienteNuevos.add(row[i].value)
        #    print("Dentro For\n lislistaEstadosVerificados:",listaEstadosVerificados," \n listaEstadosBusPendienteNuevos:",listaEstadosBusPendienteNuevos)
        listaEstadosBusTerminada=listaEstadosBusTerminada.union(listaEstadosBusPendienteAhora)
        listaEstadosBusPendienteNuevos=listaEstadosBusPendienteNuevos-listaEstadosBusTerminada
      #  print("Fuera For\n listaEstadosBusTerminada:",listaEstadosBusTerminada," \n listaEstadosBusPendienteNuevos:",listaEstadosBusPendienteNuevos)
        listaEstadosBusPendienteAhora.clear()
        for i in range(0,len(listaEstadosBusPendienteNuevos)):
            listaEstadosBusPendienteAhora.add(listaEstadosBusPendienteNuevos.pop())
        #print("listaEstadosBusPendienteAhora:",listaEstadosBusPendienteAhora,"listaEstadosBusPendienteNuevos",listaEstadosBusPendienteNuevos)
        if(len(listaEstadosBusPendienteAhora)==0):
            final=True
    return(listaEstadosVerificados)
              

def automataConvexo(sheetInicial):
    primerEstadoInicial=""
    for row in sheetInicial.iter_rows(min_row=2):
        if(row[0].value!=None):
            if(verprimerEstadoInicial(row[0].value)):
                primerEstadoInicial=row[0].value
                primerEstadoInicial=primerEstadoInicial[1:len(primerEstadoInicial)]
                listaEstadosIniciales.append(primerEstadoInicial)
            elif(verEstadosFinal(row[0].value)):
                estadoFinal=row[0].value
                estadoFinal=estadoFinal[1:len(estadoFinal)]
                listaEstadosFinalesIniciales.append(estadoFinal)
                listaEstadosIniciales.append(estadoFinal)
            else:
                listaEstadosIniciales.append(row[0].value)
                
    print(primerEstadoInicial)
    print(listaEstadosFinalesIniciales)
    print(listaEstadosIniciales)
    return(estadosConvexosNuevo(primerEstadoInicial,listaEstadosFinalesIniciales,listaEstadosIniciales,sheetInicial))

def obtenerFilaEstado(sheetExcel,estado):
    filaEstado=1
    estadoComparador=""
    for row in sheetExcel.iter_rows(min_row=2):
        filaEstado=filaEstado+1
        if(row[0].value!=None):
            estadoComparador=row[0].value
            if(verprimerEstadoInicial(estadoComparador)):
                estadoComparador=estadoComparador[1:len(estadoComparador)]
            elif(verEstadosFinal(estadoComparador)):
                estadoComparador=estadoComparador[1:len(estadoComparador)]
            if(estadoComparador==estado):
                break
    return filaEstado

def sonEquivalentesEstados(sheetExcel,estado1,estado2,diccionarioEntrada):
    filaEstado1=obtenerFilaEstado(sheetExcel,estado1)
    filaEstado2=obtenerFilaEstado(sheetExcel,estado2)
    sonEquivalentes=False
    for i in range(2,sheetExcel.max_column+1):
        valorPrueba1=sheet.cell(row=filaEstado1,column=i).value
        valorPrueba2=sheet.cell(row=filaEstado2,column=i).value
        if(diccionarioEntrada[valorPrueba1]==diccionarioEntrada[valorPrueba2]):
            sonEquivalentes=True
        else:
            sonEquivalentes=False
    return sonEquivalentes
              
def compararConjuntosCocientes(conjuntoCociente1,conjuntoConciente2):
    iguales=False
    for estado,conjunto in conjuntoCociente1.items():
        if conjuntoCociente1[estado]==conjuntoConciente2[estado]:
            iguales=True
        else:
            iguales=False
    return iguales        

def conjuntoCociente(sheetInicial,listaEstadosConvexos,ListaEstadosFinalesConvexos,estadoInicial):
    diccionarioEstadosConjuntoCociente1=dict(Ejemplo="Inicio")
    diccionarioEstadosConjuntoCociente1.clear()
    diccionarioEstadosConjuntoCociente2=diccionarioEstadosConjuntoCociente1.copy()
    listaEstadosNormales=listaEstadosConvexos-ListaEstadosFinalesConvexos
    for ele in listaEstadosFinalesConvexo:
        diccionarioEstadosConjuntoCociente1[ele]="0"
    for ele in listaEstadosNormales:
        diccionarioEstadosConjuntoCociente1[ele]="1"
    diccionarioEstadosConjuntoCociente2=diccionarioEstadosConjuntoCociente1.copy()
    listaNumeroConjuntos=set(diccionarioEstadosConjuntoCociente1.values())
    contadorNumeroConjuntos=len(listaNumeroConjuntos)
    indiceMaxNumeroConjuntos=contadorNumeroConjuntos-1
    contadorIgualdad=0
    print("listaNumeroConjuntos:",listaNumeroConjuntos," contadorNumeroConjuntos:",contadorNumeroConjuntos)
    print("dic1:",diccionarioEstadosConjuntoCociente1," dic2:",diccionarioEstadosConjuntoCociente2)
    while(contadorIgualdad<=3):
        for conjunto in listaNumeroConjuntos:
            print("listaNumConj",listaNumeroConjuntos)
            estadosEvaluar=set()
            estadosCambiar=set()
            for estado in listaEstadosConvexos:
                if diccionarioEstadosConjuntoCociente1[estado]==conjunto:
                    estadosEvaluar.add(estado)
            print("EstadosEvaluar:",estadosEvaluar)
            for estado1eva in estadosEvaluar:
                for estado2eva in estadosEvaluar:
                    if estado1eva!=estado2eva:
                        if(sonEquivalentesEstados(sheetInicial,estado1eva,estado2eva,diccionarioEstadosConjuntoCociente1)):
                            print(sonEquivalentesEstados(sheetInicial,estado1eva,estado2eva,diccionarioEstadosConjuntoCociente1))
                            estadosCambiar.add(estado1eva)
                            estadosCambiar.add(estado2eva)
            print("Estados cambiar",estadosCambiar)
            if(len(estadosCambiar)==0):
                pass
            else:
                indiceMaxNumeroConjuntos=indiceMaxNumeroConjuntos+1
                for est,con in diccionarioEstadosConjuntoCociente1.items():
                    if (est in estadosCambiar):
                        diccionarioEstadosConjuntoCociente2[est]=str(indiceMaxNumeroConjuntos)
        print("diccio1:",diccionarioEstadosConjuntoCociente1," diccio2:",diccionarioEstadosConjuntoCociente2)
        print("COMPARADOdIC",compararConjuntosCocientes(diccionarioEstadosConjuntoCociente1,diccionarioEstadosConjuntoCociente2))
        if (compararConjuntosCocientes(diccionarioEstadosConjuntoCociente1,diccionarioEstadosConjuntoCociente2)):
            contadorIgualdad=contadorIgualdad+1
            diccionarioEstadosConjuntoCociente1=diccionarioEstadosConjuntoCociente2.copy()
        else:
            contadorIgualdad=0
            diccionarioEstadosConjuntoCociente1=diccionarioEstadosConjuntoCociente2.copy()
            listaNumeroConjuntos=set(diccionarioEstadosConjuntoCociente1.values())
            contadorNumeroConjuntos=len(listaNumeroConjuntos)
            indiceMaxNumeroConjuntos=contadorNumeroConjuntos-1
    print("dict",diccionarioEstadosConjuntoCociente1)
        
        


#Menu

FILEPATHUSUARIO=input("Escriba el la direccion del archivo excel:\n")
SHEETUSUARIO=input("Escriba el nombre de la hoja de calculo en excel:\n")
workbook=load_workbook(FILEPATHUSUARIO)
sheet=workbook[SHEETUSUARIO]
listaEstadosAutomataConvexo=automataConvexo(sheet)
setListaEstadosIniciales=set(listaEstadosIniciales)
listaEstadosDesechadosConvexo=setListaEstadosIniciales-listaEstadosAutomataConvexo
listaEstadosFinalesConvexo=set(listaEstadosFinalesIniciales)-listaEstadosDesechadosConvexo
print(listaEstadosAutomataConvexo)
conjuntoCociente(sheet,listaEstadosAutomataConvexo,listaEstadosFinalesConvexo,primerEstadoInicial)
