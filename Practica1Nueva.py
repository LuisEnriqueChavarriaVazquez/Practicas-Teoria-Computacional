#Primera parte => En esta sección he creado la estructura basica de un alfabeto.


"""

Teoria Computacional // 2CM2

**** Chavarria Vazquez Luis Enrique 
**** Machorro Vences Ricardo Alberto

a) Leer el alfabeto ∑1 que servirá como base para resolver esta práctica. El alfabeto debe tener al menos tres símbolos. Los símbolos deben poder ser ingresados de dos maneras posibles
b) Leer el alfabeto
c) Leer dos cadenas: w1 y w2 ambas elementos del alfabeto ∑1. Las cadenas deben ser validadas por el programa: en caso de error en el ingreso de las
cadenas, se debe hacer la indicación al usuario para que vuelva a ingresar la cadena de forma correcta. Una cadena es inválida si contiene algún símbolo queno pertenezca al alfabeto
d) Generar la concatenacion de w1 y w2 elevado a un exponente N
e) Obtener el numero de ocurrencias de x en w1
f) Indicar si w1 es un prefijo o sufijo (propio o no propio), o subcadena, o subsecuencia, o cualquier combinación anterior, de w2
g) Leer la palabra w3 y desplegar en pantalla si esta cadena es o no es un palíndromo.
h) Elevar el alfabeto 1 a la N potencia positiva.
i) Generar tres palabras valadas para Alfabeto 1 y alfabeto 2

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
alfabeto1 = [""]
alfabeto2 = [""]

#Palabras W1,W2 generales
primeraPalabra = ''
segundaPalabra = ''

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


#Metodo para confirmar pertenencia abecedario
def perteneceAlfabeto(palabra,alfabeto):
    pertenece=0
    contadorAgrupado=0
    for i in range(0,len(alfabeto)):
        if palabra.count(alfabeto[i])>0:
            contadorAgrupado=contadorAgrupado+palabra.count(alfabeto[i])*len(alfabeto[i])
    if contadorAgrupado==len(palabra):
        pertenece=1
    return pertenece

#INCISO B
#metodo para detectar ocurrencias de un elemento en una palabra de un abecedario
def ocurrenciasLetraABC(abecedario,caracter,palabra):
    if caracter in abecedario:
        return palabra.count(caracter) ##Comprobamos si es parte y contamos
    else:
        return -1
#detecion de un palindromo
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

#ElevacionPalabra  INCISO A
def elevarExponente(primeraPalabra,segundaPalabra):
    #Pedimos al usuario un numero para el exponente
    nExponencial = int(input(f"{linea}Indique el valor del exponente n [Puede ser un valor negativo o positivo] = "))

#En este parte validamos
    if nExponencial >= 1:
        #Concatenamos y elevamos al exponente
        nuevaPalabraExponenciada = primeraPalabra + segundaPalabra
        nuevaPalabraExponenciada *= nExponencial
    elif nExponencial < 0:
        #Concatenamos, invertimos y despues simplemente tenemos que elevar
        nuevaPalabraExponenciada = primeraPalabra + segundaPalabra
        nuevaPalabraExponenciada = ((nuevaPalabraExponenciada)[::-1])
        nExponencial = (nExponencial * (-1))
        nuevaPalabraExponenciada *= nExponencial

    print(f"{linea}\nEl resultado es : " + nuevaPalabraExponenciada)

#Elevar un alfabeto N veces

def potenciaAlfabeto(numero,alfabeto,base):
    if numero == 0:
        print("")
        return
    if numero > 1:
        for palabra in alfabeto1:
            potenciaAlfabeto((numero-1),alfabeto,base + str(palabra)) #n PARAMETRO QUE NOS AYUDA CON LOS CASOS BASE
            # PALABRA CONCATENADA CON LA BASE PARA PODER QUE LOS GRUPOS TENGAN SENTIDO
    else:
        for palabra in alfabeto1:
            print(base + str(palabra), end = ",") #Para la parte de los espacio end no permite que haga salto de linea

def elevaAlfabetoPotencia(alfabeto1):
    while 1 == 1:
        nExponencialAlfabeto = int(input(f"{linea}¿Cuantas veces desea elevar a un exponente el alfabeto"))
        try:
            if nExponencialAlfabeto > 0:
                break
            print ("El numero es correcto")
        except ValueError:
            print("El numero es incorrecto")
    potenciaAlfabeto(nExponencialAlfabeto,alfabeto1,"") # "" Simplemente es un elemento intermedio"

#INCISO C
#sufijos,prefijos y subcadenas
def encontrarPrefijoSufijoSubcadena(palabra,subPalabra): #(W2 == PALABRA ,W1 == SUBPALABRA)
    if subPalabra in palabra: #Validamos si se encuentra en la palabra
        if palabra == subPalabra or subPalabra == "": #validamos si no es del tipo propio
            if palabra.startswith(subPalabra):  #validamos la parte de sufijos, prefijos y subacadenas no propias
                if palabra.endswith(subPalabra):
                    return f"{linea}Es un subfijo, prefijo y subcadena"
                else:
                    return f"{linea}Es un prefijo"
            elif palabra.endswith(subPalabra):
                return f"{linea}Es un sufijo"

            else:
                return f"{linea}Es una subcadena"
        else: #parte donde daremos tratamiento a las propias
            if palabra.startswith(subPalabra):  
                if palabra.endswith(subPalabra):
                    return f"{linea}Es un subfijo, prefijo y subcadena propia"
                else:
                    return f"{linea}Es un prefijo propio"
            elif palabra.endswith(subPalabra):
                return f"{linea}Es un sufijo propio"

            else:
                return f"{linea}Es una subcadena propia"
    else:
        #Validar la subsecuencia
        p1 = len(subPalabra) 
        p2 = len(palabra) 
        if verificarSubsecuencia(subPalabra, palabra, p1, p2): 
            return("Es una subsecuencia")
        else: 
            return("No es subsecuencia ni tampoco un prefijo,sufijo o subcadena ya que algun caracter no encaja")
        

def verificarSubsecuencia(primeraPalabra, segundaPalabra, p1, p2): 
    # casos base
    if p1 == 0:    
        return True
    if p2 == 0:    
        return False
  
    # Verificar si los caracteres empatan
    if primeraPalabra[p1-1] == segundaPalabra[p2-1]: 
        return verificarSubsecuencia(primeraPalabra, segundaPalabra, p1-1, p2-1) 
  
    # Verificar si los caracteres no empatan
    return verificarSubsecuencia(primeraPalabra, segundaPalabra, p1, p2-1) 


#GenerarPalabrasRandom
def generadorPalabrasRandom(alfabetoEntrada1,alfabetoEntrada2):
    listaPalabras=[]
    while len(listaPalabras)<3:
        palabra=""
        sizePalabra=random.randrange(1,8)
        alfabetoSelecion=random.randrange(1,3)
        if alfabetoSelecion==1:
            for i in range(0,sizePalabra):
                palabraSelecccion=alfabetoEntrada1[random.randrange(0,len(alfabetoEntrada1))]
                palabra=palabra+palabraSelecccion
            listaPalabras.append(palabra)
        elif alfabetoSelecion==2:
            for i in range(0,sizePalabra):
                palabraSelecccion=alfabetoEntrada2[random.randrange(0,len(alfabetoEntrada2))]
                palabra=palabra+palabraSelecccion
            listaPalabras.append(palabra)
    return listaPalabras
        

#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
 
    print(f"""
            {linea} Menu principal:
                [1] Generar Alfabetos (\u03A3).
                [2] Leer Alfabetos (\u03A3).
                [3] Operaciones disponibles para los alfabetos.
                [4] Limpiar Alfabetos (\u03A3).
                [5] Salir.  
        """)
     
    print (f"{linea} Seleccione la opción.")

    opcionMenuPrincipal = pedirNumeroEntero()

##Validacion para la opcion 3 ##COMPRUEBA QUE INGRESEMOS ELEMENTOS VALIDOS PARA EL ALFABETO 1 Y 2
    if opcionMenuPrincipal == 1:
        
        opcionGenerarAlfabetos=0

        print(f"""
            {linea} Menu generar alfabetos:
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
        print("\u25A0 Abecedario 1:",alfabeto1)
        print("\u25A0 Abecedario 2:",alfabeto2)
    elif opcionMenuPrincipal==3:
        palabrasCorrectas=0
        while palabrasCorrectas==0:
            print("Escriba dos palabras, un perteneciente al primer abecedario (w1) y otra al segundo (w2)")
            primeraPalabra=input(f"{linea} Escriba la palabra w1 = ")
            segundaPalabra=input(f"{linea} Escriba la palabra w2 = ")
            if perteneceAlfabeto(primeraPalabra,alfabeto1)==1 and perteneceAlfabeto(segundaPalabra,alfabeto2)==1: ##Retornara 1 en caso de no encajar
                salir_2 = False
                while not salir_2:
                    palabrasCorrectas=1
                    opcionMenuPrincipal_2 = 0
                    print("""
                
                    Datos de salida con las palabras 
                
                    [1] Escribir (w1w2) ^n con n siendo postiva o negativa
                    [2] Numero de ocurrencias de un caracter a seleccionar en w1
                    [3] Indicador si w1 es un prefijo,subfijo,subcadena o subsencuencia de w2
                    [4] Verificar si una palabra es un palindromo
                    [5] Generar  (\u03A3)^n con n siendo mayor que cero
                    [6] Generar 3 palabras validas de forma aleatroia de (\u03A3)1 y (\u03A3)2
                    [7] Salir de este menu
                
                    """)
                    
                    opcionMenuPrincipal_2 = int(input(f"{linea}Seleccione una opcion ="))

                    ##Segundo menu despues de haber validado la opcion 3

                    #[1] Escribir (w1w2) ^n con n siendo postiva o negativa
                    if  opcionMenuPrincipal_2 == 1:
                        elevarExponente(primeraPalabra,segundaPalabra)
                    #[2] Numero de ocurrencias de un caracter a seleccionar en w1
                    elif opcionMenuPrincipal_2 == 2:
                        caracterBuscar=input("Escriba el caracter a buscar:")
                        if caracterBuscar not in alfabeto1:
                            print(f"{linea} El caracter no pertenence al abecedario 1")
                        else:
                            print(f"{linea}El numero de ocurrencias de ",caracterBuscar," es :",ocurrenciasLetraABC(alfabeto1,caracterBuscar,primeraPalabra))
                    #[3] Indicador si w1 es un prefijo,subfijo,subcadena o subsencuencia de w2
                    elif opcionMenuPrincipal_2 == 3:
                        print(encontrarPrefijoSufijoSubcadena(segundaPalabra,primeraPalabra))
                    #[4] Verificar si una palabra es un palindromo
                    elif opcionMenuPrincipal_2 == 4:
                        palindromoVerificar=input("Escriba el posible palindromo:")
                        if deteccionPalindromo(palindromoVerificar)==1:
                            print(f"{linea}Es palindromo")
                        elif deteccionPalindromo(palindromoVerificar)==0:
                            print(f"{linea}No es palindromo")
                    #[5] Generar  (\u03A3)^n con n siendo mayor que cero
                    elif opcionMenuPrincipal_2 == 5:
                        elevaAlfabetoPotencia(alfabeto1)
                    #Generar 3 palabras validas de forma aleatroia de (\u03A3)1 y (\u03A3)2
                    elif opcionMenuPrincipal_2 == 6:
                        print(generadorPalabrasRandom(alfabeto1,alfabeto2))
                    elif opcionMenuPrincipal_2 == 7:
                        salir_2 = True
                    else:
                        print("Por favor ingrese un valor valido.")
            else:
                print(f"{linea}Las palabras no pertenecen a su respectivos alfabetos")
    elif opcionMenuPrincipal == 4:
        alfabeto1 = []
        alfabeto2 = []
    elif opcionMenuPrincipal == 5:
        salir = True
    else:
        print("Por favor ingrese un valor valido")