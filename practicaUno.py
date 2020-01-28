#Primera parte => En esta sección he creado la estructura basica de un alfabeto.

#Declaracion de los imports
    #Librerias de Python
import string
import sys

#Inicializo una lista vacia
alfabeto1 = []

#Declaracion de las variables de rango.
initialRange = 0
finalRange = 0
DEAFAULT_INITIAL_RANGE = 0
DEAFAULT_FINAL_RANGE = 26

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
 
salir = False
opcion = 0

#Ciclo para el menu

while not salir:
 
    print ("1. Generar Alfabeto (\u03A3)")
    print ("2. Leer el Alfabeto (\u03A3)")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    #Opcion 1: Generar el alfabeto por rango y por forma individual
    if opcion == 1:
        print("""¿Como desea generar su alfabeto (\u03A3):
                    Opcion 1: Por default de la A a la Z en minusculas
                    Opcion 2: Por default de la A a la Z en mayusculas
                    Opcion 3: Por un rango especifico dentro del intervalo con minusculas""")
        opcionPrimerApartado = int(input("Que opcion desea? = "))
        if opcionPrimerApartado == 1:
            #Llenamos el alfabeto con metodo Naive...
            item = 'a'
            for i in range(DEAFAULT_INITIAL_RANGE,DEAFAULT_FINAL_RANGE):
                alfabeto1.append(item)
                item = chr(ord(item) + 1)
        elif opcionPrimerApartado == 2:
            alfabeto1 = list(string.ascii_uppercase)
        elif opcionPrimerApartado == 3:
            initialRange = int(input("Que valor desea para el rango inicial = "))
            finalRange = int (input("Que valor desea para el rango final = "))
            #Llenamos el alfabeto con metodo Naive...
            item = 'a'
            for i in range(initialRange,finalRange):
                alfabeto1.append(item)
                item = chr(ord(item) + 1)

    elif opcion == 2:
        #Imprimimos nuestro alfabeto despues de la insercion.
        print("Este es el afabeto \u03A31   ==> " + str(alfabeto1))
        
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero valido en el rango de opciones")
 
print ("Fin")