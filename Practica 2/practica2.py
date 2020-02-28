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
import re

sys.setrecursionlimit(80000)

#Listas referencias
letrasMay=list(string.ascii_uppercase)  #Estamos guardando todo el conjunto de elementos en uppercase
letrasMin=list(string.ascii_lowercase) #estamos guardando todo el conjunto de elemento en lower
numerosList=list(str(i) for i in range(0,10) )

#Inicializando listas vacias
alfabetoRef = [""]

#expresion regular
alphabetRepeated = '^((((([b-df-hj-np-tv-z]*)(a+)([b-df-hj-np-tv-z]*))+)((([b-df-hj-np-tv-z]*)(e+)([b-df-hj-np-tv-z]*))+)((([b-df-hj-np-tv-z]*)(i+)([b-df-hj-np-tv-z]*))+)((([b-df-hj-np-tv-z]*)(o+)([b-df-hj-np-tv-z]*))+)((([b-df-hj-np-tv-z]*)(u+)([b-df-hj-np-tv-z]*))+)))+$'

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
        SalidaRepeticion=0
        #j=0
        while (SalidaRepeticion==0):
            j=0
            palabraPosible=""
            while(j< int(longitudPalabras)):
                j+=1
                palabraSeleccion=alfabetoEnt[random.randrange(0,len(alfabetoEnt))]
                palabraPosible=palabraPosible+palabraSeleccion
            if palabraPosible not in lenguajeSalida:
                SalidaRepeticion=1
            else:
                SalidaRepeticion=0     
        lenguajeSalida.append(palabraPosible)
    return lenguajeSalida


def elevaLenguajePotencia(lenguajeEntrada,exponenteEntrada):
    if exponenteEntrada==0:
        print("[ ]")
    elif exponenteEntrada <= 5 and exponenteEntrada > 0 :
        potenciaLenguaje(exponenteEntrada,lenguajeEntrada,"")
    elif exponenteEntrada >= -5 and exponenteEntrada < 0:
        lenguajeReverse=list(lenguajeEntrada[i] [::-1] for i in range(0,len(lenguajeEntrada)))
        potenciaLenguaje(exponenteEntrada*(-1),lenguajeReverse,"")
    else:
        print("Escriba un valor entre 5 y -5")
    

def potenciaLenguaje(numero,lenguajeEntrada,base):
    if numero == 0:
        print("")
        return
    if numero > 1:
        for palabra in lenguajeEntrada:
            potenciaLenguaje((numero-1),lenguajeEntrada,base + str(palabra)) #n PARAMETRO QUE NOS AYUDA CON LOS CASOS BASE
            # PALABRA CONCATENADA CON LA BASE PARA PODER QUE LOS GRUPOS TENGAN SENTIDO
    else:
        for palabra in lenguajeEntrada:
            print(base + str(palabra), end = ",") #Para la parte de los espacio end no permite que haga salto de linea

##Union del lenguaje
def unionLenguajes(lenguaje1,lenguaje2):
    lenguajeUnido = lenguaje1 + lenguaje2
    #Eliminacion de elementos repetidos
    return set(lenguajeUnido)

##Concatenacion del lenguaje // Todavia no esta listo 
def concatenacionLenguajes(lenguaje1,lenguaje2):
    for i in lenguaje1:
        for j in lenguaje2:
            print(i + j, end = ",")

#Resta de elementos (LENGUAJES1 Y LENGUAJES2)
def restaLenguajes(lenguaje1,lenguaje2):
    resta =[]    
    for palabra in lenguaje1:
        if palabra not in lenguaje2:
            resta.append(palabra)     
    return resta

    #Funcion para el alfabeto con elementos repetidos
def checkTextoConVocalesRepetidas(textoVocales):
    if(re.match(alphabetRepeated,textoVocales)):
        print("\n## texto Valido")
    else:
        print("\n## texto No valido")

#Funcion generadora de CURP random
def generadorCURPRandom():
    CURPRandom=""
    letrasMay=list(string.ascii_uppercase)
    listaNombre=["RICARDO","ANDRES","ANTONIO","GERARDO","LEONARDO","NEYMAR","ANA","ENZO","ERICK","EVA","HUGO","ANGEL","DAVID","CARLOS","JOSE","ALEJANDRO","ALBERTO","ENRIQUE"]
    listaApellidosPaternos=["BAPTISTA","AYALA","AVILA","ARRIETA","ARROYO","CALVA","CARRILLO","SANCHEZ","GONZALES","MORENO","PEREZ","SERRANO","CANO","MORCILLO","PARDO","TEBAR","GONZALES","SALINAS"]
    listaApellidosMaternos=["HERNANDEZ","VARELA","ROSAS","VIVEROS","CASTELLANOS","LAGUILLO","CASADO","VELASCO","RAMOS","BARRETO","QUIROZ","AMARO","BLOCK","CORNEJO","CASTRO","PANDO","MEDINA"]
    listaVocales=["A","E","I","O","U"]
    EntidadNacimiento=["AS","BS","CL","CS","DF","GT","HG","MC","MS","NL","PL","QR","SL","TC","TL","YN","NE","BC","CC","CM","CH","DG","GR","JC","MN","NT","OC","QT","SP","SR","TS","VZ","ZS"]
    NombreRandom=listaNombre[random.randrange(0,len(listaNombre))]
    ApePaternoRandom=listaApellidosPaternos[random.randrange(0,len(listaApellidosPaternos))]
    ApeMaternoRandom=listaApellidosMaternos[random.randrange(0,len(listaApellidosMaternos))]
    CURPRandom+=ApePaternoRandom[0]
    for i in range(0,len(ApePaternoRandom)):
        if ApePaternoRandom[i] in listaVocales:
            CURPRandom+=ApePaternoRandom[i]
            break
    CURPRandom+=ApeMaternoRandom[0]
    CURPRandom+=NombreRandom[0]
    YearRandom1=str(random.randrange(0,10))
    YearRandom2=str(random.randrange(0,10))
    CURPRandom+=YearRandom1
    CURPRandom+=YearRandom2
    MesRandom1=""
    MesRandom2=""
    DiaRandom1=""
    DiaRandom2=""
    MesRandom1=random.randrange(0,2)
    if MesRandom1==0:
        MesRandom2=random.randrange(1,10)
    elif MesRandom1==1:
        MesRandom2=random.randrange(0,3)
    if MesRandom1==0 and MesRandom2==2:
        DiaRandom1=random.randrange(0,3)
        DiaRandom2=random.randrange(1,10)
    else:
        DiaRandom1=random.randrange(0,4)
        if DiaRandom1==3:
            DiaRandom2=random.randrange(0,2)
        else:
            DiaRandom2=random.randrange(1,10)
    CURPRandom+=str(MesRandom1)
    CURPRandom+=str(MesRandom2)
    CURPRandom+=str(DiaRandom1)
    CURPRandom+=str(DiaRandom2)
    SexoRandom=random.randrange(1,3)
    if SexoRandom==1:
        CURPRandom+="H"
    elif SexoRandom==2:
        CURPRandom+="M"
    CURPRandom+=EntidadNacimiento[random.randrange(0,len(EntidadNacimiento))]
    for i in range(0,len(ApePaternoRandom)):
        if ApePaternoRandom[i] not in listaVocales:
            CURPRandom+=ApePaternoRandom[i]
            break
    for i in range(0,len(ApeMaternoRandom)):
        if ApeMaternoRandom[i] not in listaVocales:
            CURPRandom+=ApeMaternoRandom[i]
            break
    for i in range(0,len(NombreRandom)):
        if NombreRandom[i] not in listaVocales:
            CURPRandom+=NombreRandom[i]
            break
    decisionLetraNumero=random.randrange(1,3)
    PrimeroHomoclave=""
    if decisionLetraNumero==1:
        PrimeroHomoclave=random.randrange(0,10)
    elif decisionLetraNumero==2:
        PrimeroHomoclave=letrasMay[random.randrange(0,len(letrasMay))]  
    SegundoHomoclave=random.randrange(0,10)
    CURPRandom+=str(PrimeroHomoclave)
    CURPRandom+=str(SegundoHomoclave)
    return CURPRandom

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
                [5] Muestra las listas creadas (L1 & L2).
                [6] Muestra los alfabetos.
                [7] Salir.  
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
            print(f"""
            {linea}[Menu Opcion 3] Eliga una de las opcciones:
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
                print("""El resultado de la union de L1 y L2 es...""")
                print(unionLenguajes(lenguaje1,lenguaje2))
            elif opcionOperaLenguajes==2:
                print("La lista concatenada es la siguiente == ")
                concatenacionLenguajes(lenguaje1,lenguaje2)
            elif opcionOperaLenguajes==3:
                restaLenguajesValue1 = restaLenguajes(lenguaje1,lenguaje2)
                print("La resta R1 del lenguaje es (L1-L2) == ")
                print(restaLenguajesValue1)

                restaLenguajesValue2 = restaLenguajes(lenguaje2,lenguaje1)
                print("La resta R2 del lenguaje es (L2-L1) == ")
                print(restaLenguajesValue2)
            elif opcionOperaLenguajes==4:
                salidaMenuExpoLenguajes=0
                while salidaMenuExpoLenguajes==0:
                    print("Seleccione la opcion:")
                    print("[1] Elevar el lenguaje 1")
                    print("[2] Elevar el lenguaje 2")
                    opcLenguajeElevadoExpo=pedirNumeroEntero()
                    if opcLenguajeElevadoExpo==1:
                        print("Escriba un exponente entre +5 y -5")
                        opcLenguajeExpo=pedirNumeroEntero()
                        if(opcLenguajeExpo <= 5 and opcLenguajeExpo>=-5):
                            elevaLenguajePotencia(lenguaje1,opcLenguajeExpo)
                            salidaMenuExpoLenguajes=1
                        else:
                            print("El exponente esta fuera de rango")
                    elif opcLenguajeElevadoExpo==2:
                        print("Escriba un exponente entre +5 y -5")
                        opcLenguajeExpo=pedirNumeroEntero()
                        if(opcLenguajeExpo <= 5 and opcLenguajeExpo>=-5):
                           elevaLenguajePotencia(lenguaje2,opcLenguajeExpo)
                           salidaMenuExpoLenguajes=1
                        else:
                            print("El exponente esta fuera de rango")
                    else:
                        print("Eliga una opccion mencionada")
            elif opcionOperaLenguajes==5:
                print("El CURP random es:",generadorCURPRandom())
            elif opcionOperaLenguajes==6:
                textoVocales = str(input("Ingrese el texto que desea validar == "))
                checkTextoConVocalesRepetidas(textoVocales)
            elif opcionOperaLenguajes==7:
                salidaMenuOperaLenguajes=1
    elif opcionMenuPrincipal == 4:
       lenguaje1 = []
       lenguaje2 = []
    elif opcionMenuPrincipal == 5:
        print(lenguaje1)
        print(lenguaje2)

    elif opcionMenuPrincipal == 6:
        print(alfabetoRef) 
    elif opcionMenuPrincipal == 7:
        salir = True
    else:
        print("Por favor ingrese un valor valido")
