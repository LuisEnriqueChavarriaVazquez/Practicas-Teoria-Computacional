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

#Lista de las palabras W1 Y W2

primeraPalabra = ""
segundaPalabra = ""
#lista_de_palabras = []

#global listaDePalabras = []


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


#Metodo para confirmar pertenencia abecedario
def perteneceAlfabeto(palabra,alfabeto):
    pertenece=0
    for i in range(0,len(palabra)-1):
        if palabra[i] in alfabeto:
            pertenece=1
        else:
            pertenece=0
            break
    return pertenece

#Funcion para elevar al exponente n la concatenacion de dos cadenas.
#La funcion funciona hasta que implementamos la opcion 3 de operaciones (una vez que los valores en w1,w2 has sido cargados de manera satisfatoria)
#Una vez que esto fue realizado toca ejecutar la opcion en el menu que llama a nuestra funcion y este concatenara nuestra palabra y la eleva al exponente que el...
#usuario desea
def elevarExponente(primeraPalabra,segundaPalabra):
    nExponencial = int(input("Indique el valor del exponente n [Puede ser un valor negativo o positivo]"))

    nuevaPalabraExponenciada = primeraPalabra + segundaPalabra
    nuevaPalabraExponenciada *= nExponencial

    print(nuevaPalabraExponenciada)




#Ciclo para el menu

salir = False
opcionMenuPrincipal = 0

while not salir:
 
    print("""
            Menu principal:

            1. Generar Alfabetos (\u03A3).
            2. Leer Alfabetos (\u03A3).
            3. Operaciones con los alfabetos.
            4. Limpiar Alfabetos (\u03A3).
            6. Salir.
            
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
        elif opcionMenuPrincipal==2:
            print("Abecedario 1:",alfabeto1)
            print("Abecedario 2:",alfabeto2)
        elif opcionMenuPrincipal==3:
            palabrasCorrectas=0
            while palabrasCorrectas==0:
                print("Escriba dos palabras, un perteneciente al primer abecedario (w1) y otra al segundo (w2)")
                primeraPalabra=input("Escriba palabra 1:")
                segundaPalabra=input("Escriba palabra 2:")
                if perteneceAlfabeto(primeraPalabra,alfabeto1)==1 and perteneceAlfabeto(segundaPalabra,alfabeto2)==1:
                    print("comensemos")
                    palabrasCorrectas=1
                else:
                    print("Las palabras no pertenecen a su respectivos alfabetos")
                    
        #Ejecutado codigo 100 de prueba para ver si ejecuta la funcion de exponente de manera correcta
        elif opcionMenuPrincipal == 100:
            print("Ejecutado codigo 100 de prueba para ver si ejecuta la funcion de exponente de manera correcta")
            elevarExponente(primeraPalabra,segundaPalabra)
