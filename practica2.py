"""
Practica 2

Teoria Computacional // 2CM2
**** Chavarria Vazquez Luis Enrique 
**** Machorro Vences Ricardo Alberto

"""

#Declaracion de los imports
    #Librerias de Python
import string
import sys
import random

#Listas referencias
letrasMay=list(string.ascii_uppercase)  #Estamos guardando todo el conjunto de elementos en uppercase
letrasMin=list(string.ascii_lowercase) #estamos guardando todo el conjunto de elemento en lower
numerosList=list(str(i) for i in range(0,10) )

#Inicializando listas vacias
alfabetoRef = [""]

#Lenguajes vacios
lenguaje1=[""]
lenguaje2=[""]
#Linea para interfaz de consola 
#Esta parte solamente es estetica y con fines de ahorrar codigo

linea = "\u25A0"
linea *= 5

#Validacion del menu
###Simplemente verificamos que se trate de un numero

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

def valorPositivo(numeroEntr):

    if int(numeroEntr)>0:
        return 1
    else:
        return 0

#Metodo para llenar abecedario
def llenarABC():
    listaEnt=[]
    opcEntrada=0
    print(f"""
          
          {linea} Opciones de llenado de abecedario:
          1.Por rango
          2.A mano
    
    """)
    opcEntrada=pedirNumeroEntero()
    if opcEntrada==1:
        inicio=input(f"{linea} Escriba el inicio del rango:")
        fin=input(f"{linea} Escriba el fin del rango:")
        indiceInicio=0
        indiceFin=0
        if inicio in numerosList and fin in numerosList:
            indiceInicio,indiceFin=int(inicio),int(fin)+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(numerosList[i] for i in range(indiceInicio,indiceFin))
            else:
                print(f"{linea}El abecedario debe tener mas de 3 elementos")
        elif inicio in letrasMin and fin in letrasMin:
            indiceInicio,indiceFin=int(letrasMin.index(inicio)),int(letrasMin.index(fin))+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(letrasMin[i] for i in range(indiceInicio,indiceFin))
            else:
                print(f"{linea}El abecedario debe tener mas de 3 elementos")
        elif inicio in letrasMay and fin in letrasMay:
            indiceInicio,indiceFin=int(letrasMay.index(inicio)),int(letrasMay.index(fin))+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(letrasMay[i] for i in range(indiceInicio,indiceFin))
            else:
                print(f"{linea}El abecedario debe tener mas de 3 elementos")
        else:
            print(f"{linea}Los parametros de rango no pertenenecen al mismo alfabeto")
    elif opcEntrada==2:
        listaAyuda=input(f"{linea}Escriba los elementos:").split()
        if len(listaAyuda)>=3:
            listaEnt=listaAyuda
        else:
            print(f"{linea}El abecedario debe tener mas de 3 elementos")
    else:
        print(f"{linea}Eliga una opcion valida")
    
    return listaEnt

#Checar si se puede generar palabras con una longitud especifica
def checarPosibAlfabeto(alfabetoEntr,longitudPalabrasEsperado):
    minPosible=0
    for i in range(0,len(alfabetoEntr)-1):
        if minPosible<alfabetoEntr[i]:
            minPosible=len(alfabetoEntr[i])
    
    
#Metodo generar lenguaje aleatorio
def randomLenguaje(numeroPalabras,longitudPalabras,alfabetoEnt):
    lenguajeSalida=[]
    for i in range(0,int(numeroPalabras)):
        palabraPosible=""
        while(len(palabraPosible)< int(longitudPalabras)):
            palabraSeleccion=alfabetoEnt[random.randrange(0,len(alfabetoEnt))]
            palabraPosible=palabraPosible+palabraSeleccion
        print(palabraPosible)
        print(lenguajeSalida)
        lenguajeSalida.append(palabraPosible)
    return lenguajeSalida


def elevaAlfabetoPotencia(alfabetoEntrada,exponente):
    if exponente==0:
        print("[ ]")
    elif exponente <= 5 and exponente > 0 :
        potenciaAlfabeto(exponente,alfabetoEntrada,"")
    elif exponente >= -5 and exponente < 0:
        alfabetoReverse=list(alfabetoEntrada[i] [::-1] for i in range(0,len(alfabetoEntrada)-1))
        potenciaAlfabeto(exponente,alfabetoReverse,"")
    else:
        print("Escriba un valor entre 5 y -5")
    

def potenciaAlfabeto(numero,alfabetoEntrada,base):
    if numero == 0:
        print("")
        return
    if numero > 1:
        for palabra in alfabetoEntrada:
            potenciaAlfabeto((numero-1),alfabetoEntrada,base + str(palabra)) #n PARAMETRO QUE NOS AYUDA CON LOS CASOS BASE
            # PALABRA CONCATENADA CON LA BASE PARA PODER QUE LOS GRUPOS TENGAN SENTIDO
    else:
        for palabra in alfabetoEntrada:
            print(base + str(palabra), end = ",") #Para la parte de los espacio end no permite que haga salto de linea

#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
 
    print(f"""
            {linea} Menu principal:
                [1] Generar Alfabeto (\u03A3).
                [2] Generar lenguajes (\u03A3).
                [3] Operaciones disponibles para los lenguajes.
                [4] Limpiar lenguajes (\u03A3).
                [5] Salir.  
        """)
     
    print (f"{linea} Seleccione la opción.")

    opcionMenuPrincipal = pedirNumeroEntero()

##Validacion para la opcion 3 ##COMPRUEBA QUE INGRESEMOS ELEMENTOS VALIDOS PARA EL ALFABETO 1 Y 2
    if opcionMenuPrincipal == 1:
       alfabetoRef=llenarABC()
       print("EL alfabeto es ",alfabetoRef)
    elif opcionMenuPrincipal == 2:
        opcionAlfabetos=0
        print("Escriba la opccion deseasa")
        print("[1]Generar el lenguaje 1")
        print("[2]Generar el lenguaje 2")
        opcionAlfabetos=pedirNumeroEntero()
        if (opcionAlfabetos==1):
            numerosPositivos=0
            numeroPalabrasAlf1=0
            longitudPalabrasAlf1=0
            while(numerosPositivos==0):
                numeroPalabrasAlf1=input("Escriba el numero de palabras:")
                longitudPalabrasAlf1=input("Escriba la longitud de palabras:")
                if(valorPositivo(numeroPalabrasAlf1)==1 and valorPositivo(longitudPalabrasAlf1)==1):
                    numerosPositivos=1
                else:
                    print("Escriba valores correctos")
                    numerosPositivos=0

            lenguaje1=randomLenguaje(numeroPalabrasAlf1,longitudPalabrasAlf1,alfabetoRef)
            print("El lenguaje 1 es:",lenguaje1)
        elif (opcionAlfabetos==2):
            numerosPositivos=0
            numeroPalabrasAlf2=0
            longitudPalabrasAlf2=0
            while(numerosPositivos==0):
                numeroPalabrasAlf2=input("Escriba el numero de palabras:")
                longitudPalabrasAlf2=input("Escriba la longitud de palabras:")
                if(valorPositivo(numeroPalabrasAlf2)==1 and valorPositivo(longitudPalabrasAlf2)==1):
                    numerosPositivos=1
                else:
                    print("Escriba valores correctos")
                    numerosPositivos=0

            lenguaje2=randomLenguaje(numeroPalabrasAlf2,longitudPalabrasAlf2,alfabetoRef)
            print("El lenguaje 2 es:",lenguaje2)
    elif opcionMenuPrincipal == 3:
        salidaMenuOperaLenguajes=0
        opcionOperaLenguajes=0
        while(salidaMenuOperaLenguajes==0):
            print("""
            Eliga una de las opcciones:
            [1] Lenguaje resultado de la unión del lenguaje 1 y el lenguaje 2
            [2] Lenguaje resultado de la concatenacion del lenguaje 1 y el lenguaje 2
            [3] Lenguaje resultado de la diferencia del lenguaje 1 y el lenguaje 2
            [4] Lenguaje potencia del lenguaje 1 o lenguaje 2 con potencia entre +5 y -5
            [5] CURP Aleatoria
            [6] Expresiones reguales extra
            [7] Salir
            """)
            opcionOperaLenguajes=pedirNumeroEntero()
            if opcionOperaLenguajes==1:
                pass
            elif opcionOperaLenguajes==2:
                pass
            elif opcionOperaLenguajes==3:
                pass
            elif opcionOperaLenguajes==4:
                pass
            elif opcionOperaLenguajes==5:
                pass
            elif opcionOperaLenguajes==6:
                salidaMenuOperaLenguajes=1
       
    elif opcionMenuPrincipal == 4:
        lenguaje1=[]
        lenguaje2=[]
    elif opcionMenuPrincipal == 5:
        salir = True
    else:
        print("Por favor ingrese un valor valido")
