import string
import sys
import random

##Definiciones propias
from stateDefinition import stateItself
from stateDefinition import automataDefinition

linea = "\u25A0"
linea *= 5
lineaBigger = linea
lineaBigger *= 15
listaNumeros=["0","1","2","3","4","5","6","7","8","9"]
lenguajeIncisoDos = []
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(f"{linea} Introduzca un numero de opcion que desea = "))
            correcto=True
        except ValueError:
            print('Error !!, introduzca un numero entero valido')
     
    return num


### Evaluacion de la cadena de numeros
def evaluarNumero(cadenaEntrada):
     Puntero=0
     existeE=0
     existePunto=0
     existeUnNumero=0
     if cadenaEntrada[Puntero]=="+" or cadenaEntrada[Puntero]=="-":
         Puntero=Puntero+1
     for i in range(Puntero,len(cadenaEntrada)):
        Puntero=i
        if existeUnNumero==0 and cadenaEntrada[i] in listaNumeros:
            existeUnNumero=1
        if cadenaEntrada[i] not in listaNumeros:
            break
     if existeUnNumero==0:
         print("Cadena rechazada")
     elif Puntero==len(cadenaEntrada)-1 and cadenaEntrada[Puntero] in listaNumeros:
         print("Cadena aceptada")
     elif cadenaEntrada[Puntero]=="E" and Puntero!=len(cadenaEntrada)-1:
         if cadenaEntrada[Puntero+1]=="+" or cadenaEntrada[Puntero+1]=="-":
              Puntero=Puntero+1
         for l in range(Puntero+1,len(cadenaEntrada)):
             Puntero=l
             if cadenaEntrada[l] not in listaNumeros:
                 print("Cadena rechazada")
                 break
             if Puntero==len(cadenaEntrada)-1:
                 print("Cadena aceptada")
     elif cadenaEntrada[Puntero]=="." and Puntero!=len(cadenaEntrada)-1:
         existeUnNumero=0
         for j in range(Puntero+1,len(cadenaEntrada)):
             Puntero=j
             if existeUnNumero==0 and cadenaEntrada[j] in listaNumeros:
                 existeUnNumero=1
             if cadenaEntrada[j] not in listaNumeros:
                 break
         if existeUnNumero==0:
             print("Cadena rechazada")
         elif Puntero==len(cadenaEntrada)-1 and cadenaEntrada[Puntero] in listaNumeros:
             print("Cadena aceptada")
         elif cadenaEntrada[Puntero]=="E" and Puntero!=len(cadenaEntrada)-1:
             if cadenaEntrada[Puntero+1]=="+" or cadenaEntrada[Puntero+1]=="-":
                 Puntero=Puntero+1
             soloNumeros=0
             for l in range(Puntero+1,len(cadenaEntrada)):
                 Puntero=l
                 if cadenaEntrada[l] not in listaNumeros:
                     print("Cadena rechazada")
                     break
             if Puntero==len(cadenaEntrada)-1:
                 print("Cadena aceptada")
         elif (cadenaEntrada[Puntero]=="+" or cadenaEntrada[Puntero]=="-") and Puntero!=len(cadenaEntrada)-1:
             Puntero=Puntero+1
             for l in range(Puntero,len(cadenaEntrada)):
                 Puntero=l
                 if cadenaEntrada[l] not in listaNumeros:
                     print("Cadena rechazada")
                     break
                 if Puntero==len(cadenaEntrada)-1:
                     print("Cadena aceptada")
         else:
             print("Cadena Rechazada")
     else:
         print("Cadena rechazada")


### Evaluacion de la cadena de letra
def evaluarCadenaABC(cadenaEntrada):
    coleccionABC=['a','b','c']
    if len(cadenaEntrada)==3:
        if cadenaEntrada[0]=='a':
            if cadenaEntrada[1]=='a' and cadenaEntrada[2] in coleccionABC:
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='b' and cadenaEntrada[2]=='b':
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='c' and cadenaEntrada[2]=='c':
                print("Cadena aceptada")
            else:
                print("Cadena rechazada")
        elif cadenaEntrada[0]=='b':
            if cadenaEntrada[1]=='b' and cadenaEntrada[2] in coleccionABC:
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='a' and cadenaEntrada[2]=='a':
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='c' and cadenaEntrada[2]=='c':
                print("Cadena aceptada")
            else:
                print("Cadena rechazada")
        elif cadenaEntrada[0]=='c':
            if cadenaEntrada[1]=='c' and cadenaEntrada[2] in coleccionABC:
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='a' and cadenaEntrada[2]=='a':
                print("Cadena aceptada")
            elif cadenaEntrada[1]=='b' and cadenaEntrada[2]=='b':
                print("Cadena aceptada")
            else:
                print("Cadena rechazada")
        else:
            print("Cadena rechazada")
    else:
        print("Cadena rechazada")

### Evaluacion de la cadena binaria
def evaluarBinario(lenguajeIncisoDos,secondAutomataDefined):
    contadorAutomataStatePosition = 0

    while contadorAutomataStatePosition < len(lenguajeIncisoDos):
        for character in lenguajeIncisoDos[contadorAutomataStatePosition]:
            secondAutomataDefined.transicion(int(character))
        contadorAutomataStatePosition += 1

        if secondAutomataDefined.estadoNombre in lstAceptados:
            print("Cadena valida")
        else:
            print("Tu cadena es invalida")
            secondAutomataDefined=automataDefinition(secondAutomataListOfStates)

    
## Definiciones de estados del Segundo AUTOMATA
stateItself0=stateItself([[0,"ESTADO_1"],[1,"ESTADO_3"]],"ESTADO_0")
stateItself1=stateItself([[0,"ESTADO_2"],[1,"ESTADO_4"]],"ESTADO_1")
stateItself2=stateItself([[0,"ESTADO_1"],[1,"ESTADO_6"]],"ESTADO_2")
stateItself3=stateItself([[0,"ESTADO_1"],[1,"ESTADO_5"]],"ESTADO_3")
stateItself4=stateItself([[0,"ESTADO_2"],[1,"ESTADO_5"]],"ESTADO_4")
stateItself5=stateItself([[0,"ESTADO_5"],[1,"ESTADO_5"]],"ESTADO_5")
stateItself6=stateItself([[0,"ESTADO_1"],[1,"ESTADO_5"]],"ESTADO_6")

secondAutomataListOfStates=[]
secondAutomataListOfStates.append(stateItself0)
secondAutomataListOfStates.append(stateItself1)
secondAutomataListOfStates.append(stateItself2)
secondAutomataListOfStates.append(stateItself3)
secondAutomataListOfStates.append(stateItself4)
secondAutomataListOfStates.append(stateItself5)
secondAutomataListOfStates.append(stateItself6)


secondAutomataDefined=automataDefinition(secondAutomataListOfStates)
lstAceptados=[]

lstAceptados.append("ESTADO_2")
lstAceptados.append("ESTADO_6")


#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
    print(f"""
     {linea} Menu principal:
     [1] Escriba un numero en notacion exponencial 
     [2] Escriba un lenguaje formada por cadenas que contengan un número par de símbolos 0, y sin símbolos 1 sucesivos para validar el correcto.
     [3] Escriba una cadena de longitud con el lenguaje compuesto por a,b,c que teng aun dos o mas palabras consecutivas
     [4] Escriba alguna de las aplicaciones del articulo Applications of Deterministic Finite Automata
     {lineaBigger }
     {linea + linea}[5] Imprimir el lenguaje del inciso 2
     {linea + linea}[6] Limpiar el lenguaje del inciso 2
     """)
    print("Seleccione una opcion")
    opcionMenuPrincipal = pedirNumeroEntero()
    contador = 0
    if opcionMenuPrincipal==1:
        cadenaEntrada=input("Numero entrada:")
        evaluarNumero(cadenaEntrada)
    elif opcionMenuPrincipal == 2:
        longitud = int(input("Defina la longitud del lenguaje =="))
        longitud -= 1
        while contador <= longitud:
            cadenaEntrada = input("""Dame una cadena con las siguientes caracteristicas: Número par de símbolos 0, y sin símbolos 1 sucesivos.
                                    ////CADENA ==""")
            lenguajeIncisoDos.append(cadenaEntrada)
            evaluarBinario(lenguajeIncisoDos,secondAutomataDefined)
            contador += 1
    elif opcionMenuPrincipal == 4:
        
    elif opcionMenuPrincipal==3:
        cadenaEntrada=input("Cadena entrada:")
        evaluarCadenaABC(cadenaEntrada)
    elif opcionMenuPrincipal == 5:
        print("El lenguaje ingresado es == ")
        print(lenguajeIncisoDos)
    elif opcionMenuPrincipal == 6:
        lenguajeIncisoDos = []
