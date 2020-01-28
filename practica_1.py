#Primera parte => En esta sección he creado la estructura basica de un alfabeto.

#Inicializo una lista vacia
alfabeto1 = []

#Llenamos el alfabeto con metodo Naive...
item = 'a'
for i in range(0,26):
    alfabeto1.append(item)
    item = chr(ord(item) + 1)

#Imprimimos nuestro alfabeto despues de la insercion.
print("Este es el afabeto 1 ==> " + str(alfabeto1))