import string
import sys
import random

linea = "\u25A0"
linea *= 5
listaNumeros=["0","1","2","3","4","5","6","7","8","9"]
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

def evaluarNumero(cadenaEntrada):
     Puntero=0
     existeE=0
     existePunto=0
     existeUnNumero=0
     for i in range(0,len(cadenaEntrada)):
        Puntero=i
        if existeUnNumero==0 and cadenaEntrada[i] in listaNumeros:
            existeUnNumero=1
        if cadenaEntrada[i] not in listaNumeros:
            break
     if existeUnNumero==0:
         print("Cadena rechazada")
     elif Puntero==len(cadenaEntrada)-1 and cadenaEntrada[Puntero] in listaNumeros:
         print("Cadena rechazada")
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
         else:
             print("Cadena Rechazada")
     else:
         print("Cadena rechazada")




#Ciclo para el menu
salir = False
opcionMenuPrincipal = 0
while not salir:
    print(f"""
     {linea} Menu principal:
     [1] Escriba un numero en notacion exponencial 
     """)
    print("Seleccione una opccion")
    opcionMenuPrincipal = pedirNumeroEntero()
    if opcionMenuPrincipal==1:
        cadenaEntrada=input("Numero entrada:")
        evaluarNumero(cadenaEntrada)
       


