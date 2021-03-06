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

#Palabras W1,W2 generales
primeraPalabra = ''
segundaPalabra = ''


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
    contadorAgrupado=0
    for i in range(0,len(alfabeto)-1):
        if palabra.count(alfabeto[i])>0:
            contadorAgrupado=contadorAgrupado+palabra.count(alfabeto[i])*len(alfabeto[i])
    if contadorAgrupado==len(palabra):
        pertenece=1
    return pertenece

def ocurrenciasLetraABC(abecedario,caracter,palabra):
    if caracter in abecedario:
        return palabra.count(caracter)
    else:
        return -1

def deteccionPalindromo(palabra):
    palindromoEs=0
    parteInicio=0
    parteFinal=len(palabra)-1
    while parteInicio<parteFinal:
        if palabra[parteInicio]==palabra[parteFinal]:
            palindromoEs=1
            parteInicio=parteInicio+1
            parteFinal=parteFinal-1
        else:
            palindromoEs=0
            break
    return palindromoEs

def elevarExponente(primeraPalabra,segundaPalabra):
    nExponencial = int(input("Indique el valor del exponente n [Puede ser un valor negativo o positivo] = "))

#En este parte validamos
    if nExponencial >= 1:
        nuevaPalabraExponenciada = primeraPalabra + segundaPalabra
        nuevaPalabraExponenciada *= nExponencial
    elif nExponencial < 0:
        nuevaPalabraExponenciada = primeraPalabra + segundaPalabra
        nuevaPalabraExponenciada = ((nuevaPalabraExponenciada)[::-1])
        nExponencial = (nExponencial * (-1))
        nuevaPalabraExponenciada *= nExponencial
    else:
        print("\nEl resultado de elevar a la cero es el elemento neutro (\u03BB)")

    print("\nEl resultado es : " + nuevaPalabraExponenciada)




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
            5. Salir.
            
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
        caracterBuscar=input("Escriba el caracter a buscar:")
        if caracterBuscar not in alfabeto1:
            print("El caracter no pertenence al abecedario 1")
        else:
            print("El numero de ocurrencias de ",caracterBuscar," es :",ocurrenciasLetraABC(alfabeto1,caracterBuscar,primeraPalabra))
        
        palindromoVerificar=input("Escriba el posible palindromo:")
        if deteccionPalindromo(palindromoVerificar)==1:
            print("Es palindromo")
        elif deteccionPalindromo(palindromoVerificar)==0:
            print("No es palindromo")
    elif opcionMenuPrincipal == 69:
        elevarExponente(primeraPalabra,segundaPalabra)

