import string
import sys
import random

import turtle
import time

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

### PARTE DE LA MAQUINA DE VENDING

"""stateItself0_2=stateItself([[0,"ESTADO_vending_1"],[1,"ESTADO_vending_2"]],"ESTADO_vending_0")
stateItself1_2=stateItself([[0,"ESTADO_vending_2"],[1,"ESTADO_vending_3"]],"ESTADO_vending_1")
stateItself2_2=stateItself([[0,"ESTADO_vending_3"],[1,"ESTADO_vending_4"]],"ESTADO_vending_2")
stateItself3_2=stateItself([[0,"ESTADO_vending_4"],[1,"ESTADO_vending_5"]],"ESTADO_vending_3")
stateItself4_2=stateItself([[0,"ESTADO_vending_3"],[1,"ESTADO_vending_6"]],"ESTADO_vending_4") ##Final
stateItself5_2=stateItself([[0,"ESTADO_vending_2"],[1,"ESTADO_vending_7"]],"ESTADO_vending_5") ##Final
stateItself6_2=stateItself([[0,"ESTADO_vending_1"],[1,"ESTADO_vending_8"]],"ESTADO_vending_6") ##Final
stateItself6_2=stateItself([[0,"ESTADO_vending_8"],[1,"ESTADO_vending_9"]],"ESTADO_vending_6") ##Final
stateItself6_2=stateItself([[0,"ESTADO_vending_8"],[1,"ESTADO_vending_7"]],"ESTADO_vending_6") ##Final

vending_AutomataListOfStates=[]
vending_AutomataListOfStates.append(stateItself0)
vending_AutomataListOfStates.append(stateItself1)
vending_AutomataListOfStates.append(stateItself2)
vending_AutomataListOfStates.append(stateItself3)
vending_AutomataListOfStates.append(stateItself4)
vending_AutomataListOfStates.append(stateItself5)
vending_AutomataListOfStates.append(stateItself6)


vending_AutomataDefined=automataDefinition(vending_AutomataListOfStates)
lstAceptados_vending=[]

lstAceptados_vending.append("ESTADO_vending_5")
lstAceptados_vending.append("ESTADO_vending_6")
lstAceptados_vending.append("ESTADO_vending_7")
lstAceptados_vending.append("ESTADO_vending_9")"""

##Validacion de los casos de la maquina de VENDING
def maquinaVending(acumulado):
    while True:
        if acumulado == .25:
            while True:
                faltante = float(input("Le falta un dolar para acompletar 1.25, ingreselo por favor = "))
                if faltante == 1.0: ##usuario nos da un dolar
                    acumulado = faltante + acumulado
                    if acumulado == 1.25:
                        print("Tome su soda!!!")
                        print("Cambio == " + str(float(acumulado)-1.25))
                        return False;
                elif faltante == .25: ##usuario nos da un .25
                    acumulado = faltante + .25
                    if acumulado == .50:
                        while True:
                            faltante = float(input("Le falta .75 para acompletar 1.25, ingreselo por favor = "))
                            if faltante == .25:
                                acumulado = faltante + .50
                                while True:
                                    faltante = float(input("Le falta .50 para acompletar 1.25, ingreselo por favor = "))
                                    if faltante == .25:
                                        acumulado = faltante + .75
                                        while True:
                                            faltante = float(input("Le falta .25 para acompletar 1.25, ingreselo por favor = "))
                                            if  faltante == .25:
                                                acumulado = faltante + 1.0
                                                if acumulado == 1.25:
                                                    print("Tome su soda!!!")
                                                    print("Cambio == " + str(float(acumulado)-1.25))
                                                    return False;
                                            elif faltante == 1.0:
                                                acumulado = faltante + 1.0
                                                if acumulado == 2.0:
                                                    print("Tome su soda y su cambio!!!")
                                                    print("Cambio == " + str(float(acumulado)-1.25))
                                                    return False;
                                            else:
                                                print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
                                    elif faltante == 1.0:
                                        acumulado = faltante + .75
                                        if acumulado == 1.75:
                                            print("Tome su soda y su cambio!!!")
                                            print("Cambio == " + str(float(acumulado)-1.25))
                                            return False
                                    else:
                                        print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
                            elif faltante == 1.0:
                                acumulado = 1.5
                                print("Tome su soda y su cambio!!")
                                print("Cambio == " + str(float(acumulado)-1.25))
                                return False;
                            else:
                                print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
                    else:
                        print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
                else:
                    print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
        elif acumulado == 1.0:
            faltante = float(input("Le falta .25 centavos para acompletar 1.25 , ingreselo por favor = "))
            if faltante == .25:
                acumulado = 1.25
                print("Tome su soda!!!")
                print("Cambio == " + str(float(acumulado)-1.25))
                return False;
            elif faltante == 1.0:
                acumulado = 2
                print("Tome su soda y su cambio!!")
                print("Cambio == " + str(float(acumulado)-1.25))
                return False;
            else:
                print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")
        else:
            print("No aceptamos esa denominacion!!! Solo .25 y 1 Dolar")

##Validamos lo que la maquina recibe
def validarDolares(cadenaEntrada):
    if cadenaEntrada == 1.0 or cadenaEntrada == .25:
        return True
    else:
        return False

##Primer contacto de la maquina
def primerBebida():
    cadenaEntrada = float(input("Ingrese una cantidad de dinero = "))
    validacion = validarDolares(cadenaEntrada)
    if validacion == True:
        print(f"""{linea} Cantidad aceptada """)
        maquinaVending(cadenaEntrada)
    else:
        print("Valor no adecuado, la maquina no acepta dichas cantidades")


### Parte del semaforo
def ejecutarSemaforo():
    ###Automata for stop light in python
    wn = turtle.Screen()
    wn.title("Luces de semaforo automata")
    wn.bgcolor("blue")

    ### Diseño de las luces ((Creacion de elementos))
    luzRoja = turtle.Turtle()
    luzRoja.shape("circle")
    luzRoja.color("grey")
    luzRoja.pensize(10)
    luzRoja.penup()
    luzRoja.goto(0,40)

    luzAmarilla = turtle.Turtle()
    luzAmarilla.shape("circle")
    luzAmarilla.color("grey")
    luzAmarilla.penup()
    luzAmarilla.goto(0,0)

    luzVerde = turtle.Turtle()
    luzVerde.shape("circle")
    luzVerde.color("grey")
    luzVerde.penup()
    luzVerde.goto(0,-40)

    ### Establecer el cambio

    while True:
        luzAmarilla.color("grey")
        luzRoja.color("red")
        time.sleep(4)
        luzRoja.color("grey")
        luzVerde.color("green")
        time.sleep(3)
        luzVerde.color("grey")
        luzAmarilla.color("yellow")
        time.sleep(2)
    ### pausar la pantalla
    wn.mainloop()


#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
    print(f"""
     {linea} Menu principal:
     [1] Escriba un numero en notacion exponencial 
     [2] Escriba un lenguaje formada por cadenas que contengan un número par de símbolos 0, y sin símbolos 1 sucesivos para validar el correcto.
     [3] Escriba una cadena de longitud con el lenguaje compuesto por a,b,c que teng aun dos o mas palabras consecutivas
     [4] Semaforo
     [5] Maquina de VENDING
     {lineaBigger }
     {linea + linea}[6] Imprimir el lenguaje del inciso 2
     {linea + linea}[7] Limpiar el lenguaje del inciso 2
     """)
    print("Seleccione una opcion")
    opcionMenuPrincipal = pedirNumeroEntero()
    contador = 0
    if opcionMenuPrincipal==1:
        cadenaEntrada=input("Numero entrada:")
        evaluarNumero(cadenaEntrada)
    elif opcionMenuPrincipal == 2:
        longitud = int(input("Defina la longitud del lenguaje == "))
        longitud -= 1
        while contador <= longitud:
            cadenaEntrada = input("""Dame una cadena con las siguientes caracteristicas: Número par de símbolos 0, y sin símbolos 1 sucesivos.
                                    ////CADENA == """)
            lenguajeIncisoDos.append(cadenaEntrada)
            evaluarBinario(lenguajeIncisoDos,secondAutomataDefined)
            contador += 1   
    elif opcionMenuPrincipal==3:
        cadenaEntrada=input("Cadena entrada:")
        evaluarCadenaABC(cadenaEntrada)
    elif opcionMenuPrincipal == 4:
        ejecutarSemaforo()
    elif opcionMenuPrincipal == 5:
        ##Validacion de la maquina de vending
        print(f"""Bienvenido a la maquina de Vending de SODAS
                /////// SOLO ACEPTAMOS 1 DOLAR Y .25 CENTAVOS
                {linea} Precio de las sodas: 1.25 """)
        primerBebida()
        masBebida = input("Desea comprar otra soda??? (Y/N)")
        if masBebida == "Y" or masBebida == "y":
            primerBebida()
        else:
            print("Gracias por su compra!!")
    elif opcionMenuPrincipal == 6:
        print("El lenguaje ingresado es == ")
        print(lenguajeIncisoDos)
    elif opcionMenuPrincipal == 7:
        lenguajeIncisoDos = []
