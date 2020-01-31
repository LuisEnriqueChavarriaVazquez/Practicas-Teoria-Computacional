""" Diseño : Gomez Salas Hugo Santiago - Flores Jimenez Edson Uriel 
    Grupo: 2CM3 	            Teoria computacional
    Nombre: Lenguajes 
    
    Problematica: 
	
    NOTAS:
    el intervalo se tiene que dar un primer elemento menor que al segundo 
    de lo contrario esta incorrecto.

    Profesor:  AGUILAR GARCIA RAFAEL """
from random import randint
import math
import re

alfabeto1 = []
lenguaje1 = []
lenguaje2 = []
lenguajeUnion=[]
lenguajeC = []
lenguajeResta1 =[]
lenguajeResta2 =[]
lenguajeAux1 =[]
lenguajeAux2 =[]
estadosAbrebiaciones = ["AS","BC","BS","CC","CS","CH","CL","CM","DF","DG","GT","GR","HG","JC","MC","MN","MS","NT","NL","OC","PL","QO","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]
estados = ["Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Coahuila","Colima","Ciudad De México","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos","Nayarit","Nuevo León","Oaxaca","Puebla","Querétaro","Quintana Roo","San Luis Potosí","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatán","Zacatecas"]

def __guadarAlfabeto__(alfabetoarray):

    print("Seleccione una opcion para el alfabeto \n")
    print("1.-Por Extencion\n")
    print("2.-Por Rango\n")
    opcion = input("Seleccion: ")
    print(opcion)

    if opcion is "1":
        n = input("Cuantos elementos tendra el alfabeto?\n")
        for x in range(0, int(n)):
            alfabetoarray.append(input("Palabra " + str(x+1) + ": "))

    elif opcion is "2":
        primero = input("Ingrese el primer elemento: \n")
        ultimo = input("Ingrese el ultimo elemento: \n")

        if ord(primero) > ord(ultimo):
            print("Invalido")
            exit(1)

        for x in range(ord(primero), ord(ultimo)+1):
            alfabetoarray.append(chr(x))

def __lenguajeRandom__(alfabeto, lenguaje, np, lngP):
    for x in range(0, np):
        while 1==1:
            palabra = ""
            for y in range(0, lngP):
                rand = randint(0, len(alfabeto)-1)
                palabra += alfabeto[rand]
            if palabra not in lenguaje:
                lenguaje.append(palabra)
                break
    
def __unionLenguaje__(lenguaje1, lenguaje2):
    lenguajeU=[]
    if len(lenguaje1) >= len(lenguaje2):
        lenguajeU+=lenguaje1
        for palabra in lenguaje2:
            if palabra not in lenguaje1:
                lenguajeU.append(palabra)
    else:
        lenguajeU+=lenguaje2
        for palabra in lenguaje1:
            if palabra not in lenguaje2:
                lenguajeU.append(palabra)
    return lenguajeU

def __restaLenguaje__(a,b):
    resta =[]    
    for palabra in a:
        if palabra not in b:
            resta.append(palabra)     
    return resta
    
def __concatAlfabeto__(n,alfabeto,base):
    if n==0:
        print("")
        return
    if n>1:
        for palabra in alfabeto:
            __concatAlfabeto__((n-1),alfabeto,palabra +str(base))

    else:
        for palabra in alfabeto:
            print(base + str(palabra),end=",")

def __calcularCurp__(nombre,apellidoP,apellidoM,dia,mes,edad,sexo,entidad):
    regexVocal = re.compile('a|e|i|o|u|A|E|I|O|U')
    curp = ""
    abreviaturaReal = ""
    curp += apellidoP[0] + regexVocal.findall(apellidoP)[0] + apellidoM[0] + nombre[0] + edad[::-1][0:2][::-1] + mes + dia + sexo
    for estado in estados:
        if estado.lower() == entidad.lower():
            abreviaturaReal = estadosAbrebiaciones[estados.index(estado)]
            
    curp += abreviaturaReal 
    for x in range(0,5):
        if x <4:
            rand =  randint(65,90-1)  
            curp += chr(rand)
        else:
            rand =  randint(0,9)
            curp += str(rand)  
    return curp.upper()
 

print("Inciso A")
__guadarAlfabeto__(alfabeto1)
print(alfabeto1)

print("Inciso B")
np1 = input("¿Cuantas palabras tendra tu alfabeto #1 aletorio?")
lngP1 = input("¿Cuantas letras tendra cada palabra del alfabeto #1?")
__lenguajeRandom__(alfabeto1, lenguaje1, int(np1), int(lngP1))
print(lenguaje1)

np2 = input("¿Cuantas palabras tendra tu alfabeto #2 aletorio?")
lngP2 = input("¿Cuantas letras tendra cada palabra del alfabeto #2?")
__lenguajeRandom__(alfabeto1, lenguaje2, int(np2), int(lngP2))
print(lenguaje2)

print("Inciso C")
print("La union de los lenguajes es :")
lenguajeUnion =__unionLenguaje__(lenguaje1,lenguaje2)
print(lenguajeUnion)

print("Inciso D")
print("La concatencion de los lenguajes es:")

for i in lenguaje1:
    for j in lenguaje2:
        print(i+j,end =",")

print("\nInciso E")
lenguajeResta1 = __restaLenguaje__(lenguaje1,lenguaje2)
print("La resta de L1-L2 es: ")
print(lenguajeResta1)

lenguajeResta2 = __restaLenguaje__(lenguaje2,lenguaje1)
print("La resta de L2-L1 es: ")
print(lenguajeResta2)

print("Inciso F")
while 1==1:
    valor=input("Dame el valor de la potencia: ")
    if int(valor)<=5 and int(valor)>=-5:
        
        if int(valor)<0:
            for palabra in lenguaje1:
                palabra = palabra[::-1]
                lenguajeAux1.append(palabra)

            for palabra in lenguaje2:
                palabra = palabra[::-1]
                lenguajeAux2.append(palabra)
            valor = math.fabs(int(valor))
            print("1.-L1\n2.-L2")
            n=input("Seleccione el lenguje: ")
            if int(n) == 1:
                __concatAlfabeto__(int(valor),lenguajeAux1,"")
            if int(n)== 2:
                __concatAlfabeto__(int(valor),lenguajeAux2,"")
            break

        else:
            print("1.-L1\n2.-L2")
            n=input("Seleccione el lenguje: ")
            if int(n) == 1:
                __concatAlfabeto__(int(valor),lenguaje1,"")
            if int(n)== 2:
                __concatAlfabeto__(int(valor),lenguaje2,"")
        break

    else:
        print("Valor invalido recuerda el valor debe ser de -5 a 5")

print("\nInciso G")
nombre=input("Nombre: ")
apellidoP=input("Apellido Paterno: ")
apellidoM =input("Apellido Materno: ")
print("Ingrese su fecha de nacimiento (16/11/2000)")
dia = input("Dia: ")
mes = input("Mes (Numerico): ")
edad = input("Año: ")
sexo=input("Sexo: ")
entidad = input("Entidad Federativa: ")
print(__calcularCurp__(nombre,apellidoP,apellidoM,dia,mes,edad,sexo,entidad))
