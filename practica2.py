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
alfabeto = [""]

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
def checarPosibAlfabeto(alfabeto,longitudPalabrasEsperado):
    minPosible=0
    for i in range(0,len(alfabeto)-1):
        if minPosible<alfabeto[i]:
            minPosible=len(alfabeto[i])
    
    
#Metodo generar lenguaje aleatorio

def randomLenguaje(numeroPalabras,longitudPalabras,alfabetoEnt):
    lenguajeSalida=[]
    for i in range(0,numeroPalabras-1):
        palabraPosible=""
        while(len(palabraPosible)< longitudPalabras):
            palabraSeleccion=alfabetoEnt[random.randrange(0,len(alfabetoEnt))]
            palabraPosible=palabraPosible+palabraSeleccion
        lenguajeSalida[i]=palabraPosible
    return lenguajeSalida





#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
 
    print(f"""
            {linea} Menu principal:
                [1] Generar Alfabeto (\u03A3).
                [2] Generar lenguajes (\u03A3).
                [3] Operaciones disponibles para los alfabetos.
                [4] Limpiar Alfabetos (\u03A3).
                [5] Salir.  
        """)
     
    print (f"{linea} Seleccione la opción.")

    opcionMenuPrincipal = pedirNumeroEntero()

##Validacion para la opcion 3 ##COMPRUEBA QUE INGRESEMOS ELEMENTOS VALIDOS PARA EL ALFABETO 1 Y 2
    if opcionMenuPrincipal == 1:
       alfabeto=llenarABC()
       print("EL alfabeto es ",alfabeto)
    elif opcionMenuPrincipal == 2:

    elif opcionMenuPrincipal == 5:
        salir = True
    else:
        print("Por favor ingrese un valor valido")