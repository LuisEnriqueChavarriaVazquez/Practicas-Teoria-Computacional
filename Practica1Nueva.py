#Primera parte => En esta sección he creado la estructura basica de un alfabeto.

#Declaracion de los imports
    #Librerias de Python
import string
import sys

#Lista referencia
letrasMin=list(string.ascii_uppercase)


#Inicializando listas vacias
alfabeto1 = []
alfabeto2 = []

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
            
            formaGeneraAlfabato1=0
            print("""
            
            ¿Como desea generar su alfabeto (\u03A3 1):
                    Opcion 1:Por rango
                    Opcion 2:De forma individual 
                    
                    """)
            formaGeneraAlfabato1=pedirNumeroEntero()
            if formaGeneraAlfabato1==1:
                pass
            elif formaGeneraAlfabato1==2:
                pass

            

       

         


