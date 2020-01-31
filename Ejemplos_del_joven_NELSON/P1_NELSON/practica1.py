""" Diseño : Gomez Salas Hugo Santiago - Flores Jimenez Edson Uriel 
    Grupo: 2CM3 	            Teoria computacional
    Nombre: Lenguajes
    
    Problematica: El usuario debe cargar 2 lenguajes ya sea que introduzca uno por uno o que 
    los coloque como un intervalo y en este pueda realizar lo siguiente:
    -Recibir 2 cadenas que pertenezcan al primer lenguaje. 
    -Concatenar dichas cadenas n veces (n puede ser tanto negativo como positivo).
    -Dar un caracter que se encuentre en el primer lenguaje y que muestre cuantas veces aparece
    en la cadena #1.
    -Verificar que la cadena 1 es un subfijo, prefijo o subcadena de la segunda cadena
    -Recibir una tercer cadena y verificar si es un palindromo.
    -Concatenar n veces el primer lenguaje (n tiene que se positivo).
    -Realizar la multiplicacion de el primer y segundo lenguaje.
	
    NOTAS:
    el intervalo se tiene que dar un primer elemento menor que al segundo 
    de lo contrario esta incorrecto.

    Profesor:  AGUILAR GARCIA RAFAEL """

"""
 ------------------------------------------------------------------------------------------------------------------------------
|													Variables																|			
|----------------------------------------------------------------------------------------------------------------------------|*/ 
"""
alfabeto1 = []
alfabeto2 = []
nuevapalabra = []

"""
 ------------------------------------------------------------------------------------------------------------------------------
|													Funciones																|			
|----------------------------------------------------------------------------------------------------------------------------|*/
"""

def __guadarAlfabeto__(alfabetoarray):

    print("Seleccione una opcion para el alfabeto \n")
    print("1.-Por Extencion\n")
    print("2.-Por Rango\n")
    opcion = input("Seleccion: ")
    print(opcion) 

    if opcion is "1": 
        n = input("Cuantos elementos tendra el alfabeto?\n")
        for x in range(0,int (n)):
            alfabetoarray.append(input("Palabra "+ str(x+1) + ": "))

    elif opcion is "2":
        primero = input("Ingrese el primer elemento: \n")
        ultimo = input("Ingrese el ultimo elemento: \n")
        
        if ord(primero)>ord(ultimo): 
            print("Invalido")
            exit (1)
        
        for x in range(ord(primero),ord(ultimo)+1):
            alfabetoarray.append(chr(x))

def __evaluarPalabra__(alfabeto,palabra):
    for elemento in alfabeto:
        palabra=palabra.replace(elemento,"")
    if palabra == "":
        return True
    else:
        return False


def __concatN__(p1,p2,n):
    
    if n == 0:
        return ""
    
    nuevapalabra = p1+p2
    nuevapalabra = nuevapalabra*abs(n)

    if n<0:
        palabraNegativa = nuevapalabra[::-1]
        return palabraNegativa

    else:
        return nuevapalabra


def ___buscarLetra__(palabra,letra):
    return palabra.count(letra)

def ___subCadenas__(palabra,subPalabra):
    if subPalabra in palabra or subPalabra =="":
        if palabra.startswith(subPalabra):  
            if palabra.endswith(subPalabra):
                return "Es un subfijo, prefijo y subcadena"
            else:
                return "Es un prefijo"

        elif palabra.endswith(subPalabra):
            return "Es un subfijo"

        else:
            return "Es una subcadena"
    
    else:
        return "No es una subcadena"

def __palindromo__(palabra):
    return palabra == palabra[::-1]

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

print("Inciso A)")
__guadarAlfabeto__(alfabeto1)
print(alfabeto1) 

print("Inciso B)")
__guadarAlfabeto__(alfabeto2)
print(alfabeto2) 

print("Inciso C)")
while 1==1:
    palabra1 = input("Escriba su cadena #1:")
    if __evaluarPalabra__(alfabeto1,palabra1):
        break
    else:
        print("Tu palabra es invalida")

while 1==1:
    palabra2 = input("Escriba su cadena #2:")
    if __evaluarPalabra__(alfabeto1,palabra2):
        break
    else:
        print("Tu palabra es invalida")  

print("Inciso D)")
concatenaciones = input("Cual sera el exponente de tu expresion: \n")
print(__concatN__(palabra1,palabra2,int(concatenaciones)))

print("Inciso E)")
while 1==1:
    letra = input("Que letra desea contar en palabra #1\n")
    if letra in alfabeto1:
        
        break
    else:
        print("La letra no se enunetra en el alfabeto 1\n")

print("Encontrado:" + str(___buscarLetra__(palabra1,letra))) 

print("Inciso F)")
print(___subCadenas__(palabra2,palabra1))
print("Inciso G)")
palabra3 = input("Escriba una palabra #3:")
if __palindromo__(palabra3):
    print("La palabra 3 es un palindromo")
else:
    print("La palabra 3 no es un palindromo")

print("Inciso H)")
while 1==1:
    nAlfabeto = input("¿Cuantas veces quieres elevar el alfabeto 1?")
    try:
        nAlfabeto=int(nAlfabeto)
        if nAlfabeto > 0:
            break
        print("entrada invalida") 
    except ValueError:
        print("entrada invalida")
__concatAlfabeto__(nAlfabeto,alfabeto1,"")

print("\nInciso I)")
for i in alfabeto1:
	for j in alfabeto2:
		print(i,j,end =",")

for i in alfabeto2:
	for j in alfabeto1:
		print(i,j,end =",")