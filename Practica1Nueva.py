#Primera parte => En esta sección he creado la estructura basica de un alfabeto.

#Declaracion de los imports
    #Librerias de Python
import string
import sys

#Listas referencias
letrasMay=list(string.ascii_uppercase)
letrasMin=list(string.ascii_lowercase)
numerosList=list(str(i) for i in range(0,10) )
#Inicializando listas vacias
alfabeto1 = [""]
alfabeto2 = [""]

#Validacion del menu

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero de opcion que desea: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero valido')
     
    return num

#Metodo para llenar abecedario
def llenarABC():
    listaEnt=[]
    opcEntrada=0
    print("""
          
          Opciones de llenado de abecedario:
          1.Por rango
          2.A mano
    
    """)
    opcEntrada=pedirNumeroEntero()
    if opcEntrada==1:
        inicio=input("Escriba el inicio del rango:")
        fin=input("Escriba el fin del rango:")
        indiceInicio=0
        indiceFin=0
        if inicio in numerosList and fin in numerosList:
            indiceInicio,indiceFin=int(inicio),int(fin)+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(numerosList[i] for i in range(indiceInicio,indiceFin))
            else:
                print("El abecedario debe tener mas de 3 elementos")
        elif inicio in letrasMin and fin in letrasMin:
            indiceInicio,indiceFin=int(letrasMin.index(inicio)),int(letrasMin.index(fin))+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(letrasMin[i] for i in range(indiceInicio,indiceFin))
            else:
                print("El abecedario debe tener mas de 3 elementos")
        elif inicio in letrasMay and fin in letrasMay:
            indiceInicio,indiceFin=int(letrasMay.index(inicio)),int(letrasMay.index(fin))+1
            if (indiceFin-indiceInicio)>=3:
                listaEnt=list(letrasMay[i] for i in range(indiceInicio,indiceFin))
            else:
                print("El abecedario debe tener mas de 3 elementos")
        else:
            print("Los parametros de rango no pertenenecen al mismo alfabeto")
    elif opcEntrada==2:
        listaAyuda=input("Escriba los elemntos:").split()
        if len(listaAyuda)>=3:
            listaEnt=listaAyuda
        else:
            print("El abecedario debe tener mas de 3 elementos")
    else:
        print("Eliga una opcion valida")
    
    return listaEnt
    

#Ciclo para el menu

salir = False
opcionMenuPrincipal = 0

while not salir:
 
    print("""
            Menu principal:

            1. Generar Alfabetos (\u03A3).
            2. Leer Alfabetos (\u03A3).
            3. Limpiar Alfabetos (\u03A3).
            4. Salir.
            
        """)
     
    print ("Elige una opcion")

    opcionMenuPrincipal = pedirNumeroEntero()

    if opcionMenuPrincipal == 1:
        
        opcionGenerarAlfabetos=0

        print("""

            Menu generar alfabetos:
            1.Generar Alfabeto 1
            2.Generar Alfabeto 2     


         """)
        opcionGenerarAlfabetos=pedirNumeroEntero()
         
        if opcionGenerarAlfabetos== 1:
            print(alfabeto1)
            alfabeto1=llenarABC()
            print(alfabeto1)
        elif opcionGenerarAlfabetos== 2:
             alfabeto2=llenarABC()
