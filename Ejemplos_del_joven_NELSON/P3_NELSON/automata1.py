from estado import estado
from estado import automata

def insertDigits(estado,destino):
    newtransition=[]
    for x in range(0,9):
        value=[str(x),destino]
        newtransition.append(value)
    estado.listado+=newtransition

def insertLetras(estado,destino):
    newtransition=[]
    for x in range(65,91):
        if x != 69:
            value=[chr(x),destino]
            newtransition.append(value)
    for x in range(97,123):
        if x != 101:
            value=[chr(x),destino]
            newtransition.append(value)
    estado.listado+=newtransition

"""Primer Automata"""
estadoD0=estado([['+',"Q1"],['-',"Q1"],['.',"Q9"]],"Q0")
insertLetras(estadoD0,"Q9")
insertDigits(estadoD0,"Q2")


estadoD1=estado([],"Q1")
insertLetras(estadoD1,"Q9")
insertDigits(estadoD1,"Q2")

estadoD2=estado([['.',"Q3"],['E',"Q9"],['e',"Q9"],['+',"Q9"],['-',"Q9"]],"Q2")
insertDigits(estadoD2,"Q2")
insertLetras(estadoD2,"Q9")

estadoD3=estado([['E',"Q9"],['e',"Q9"],['.',"Q9"],['+',"Q9"],['-',"Q9"]],"Q3")
insertDigits(estadoD3,"Q7")
insertLetras(estadoD3,"Q9")

estadoD4=estado([['E',"Q9"],['e',"Q9"],['.',"Q3"],['+',"Q8"],['-',"Q8"]],"Q4")
insertDigits(estadoD4,"Q6")
insertLetras(estadoD4,"Q9")


estadoD5=estado([['E',"Q9"],['e',"Q9"],['.',"Q9"],['+',"Q9"],['-',"Q9"]],"Q6")
insertDigits(estadoD5,"Q6")
insertLetras(estadoD5,"Q9")

estadoD6=estado([['E',"Q4"],['e',"Q4"],['.',"Q9"],['-',"Q9"],['+',"Q9"]],"Q7")
insertDigits(estadoD6,"Q7")
insertLetras(estadoD6,"Q9")

estadoD7=estado([['.',"Q9"],['+',"Q9"],['-',"Q9"]],"Q8")
insertDigits(estadoD7,"Q6")
insertLetras(estadoD7,"Q9")

estadoD8=estado([['.',"Q9"],['+',"Q9"],['-',"Q9"],['E',"Q9"],['e',"Q9"]],"Q9")
insertDigits(estadoD8,"Q9")
insertLetras(estadoD8,"Q9")

"""Segundo Automata"""
estado0=estado([[0,"Q1"],[1,"Q3"]],"Q0")
estado1=estado([[0,"Q2"],[1,"Q4"]],"Q1")
estado2=estado([[0,"Q1"],[1,"Q6"]],"Q2")
estado3=estado([[0,"Q1"],[1,"Q5"]],"Q3")
estado4=estado([[0,"Q2"],[1,"Q5"]],"Q4")
estado5=estado([[0,"Q5"],[1,"Q5"]],"Q5")
estado6=estado([[0,"Q1"],[1,"Q5"]],"Q6")

"""Tercer Automata"""
estadoA0=estado([['a',"Q1"],['b',"Q2"],['c',"Q3"],['d',"Q4"]],"Q0") 
"""Solo a"""
estadoA1=estado([['a',"Q5"],['b',"Q8"],['c',"Q9"],['d',"Q10"]],"Q1")
estadoA8=estado([['a',"Q6"],['b',"Q6"],['c',"Q7"],['d',"Q7"]],"Q8")
estadoA9=estado([['a',"Q6"],['b',"Q7"],['c',"Q6"],['d',"Q7"]],"Q9")
estadoA10=estado([['a',"Q6"],['b',"Q7"],['c',"Q7"],['d',"Q6"]],"Q10")
"""Solo b"""
estadoA2=estado([['a',"Q11"],['b',"Q5"],['c',"Q12"],['d',"Q13"]],"Q2")
estadoA11=estado([['a',"Q6"],['b',"Q6"],['c',"Q7"],['d',"Q7"]],"Q11")
estadoA12=estado([['a',"Q7"],['b',"Q6"],['c',"Q6"],['d',"Q7"]],"Q12")
estadoA13=estado([['a',"Q7"],['b',"Q6"],['c',"Q7"],['d',"Q6"]],"Q13")
"""Solo c"""
estadoA3=estado([['a',"Q14"],['b',"Q15"],['c',"Q5"],['d',"Q16"]],"Q3")
estadoA14=estado([['a',"Q6"],['b',"Q7"],['c',"Q6"],['d',"Q7"]],"Q14")
estadoA15=estado([['a',"Q7"],['b',"Q6"],['c',"Q6"],['d',"Q7"]],"Q15")
estadoA16=estado([['a',"Q7"],['b',"Q7"],['c',"Q6"],['d',"Q6"]],"Q16")
"""Solo d"""
estadoA4=estado([['a',"Q17"],['b',"Q18"],['c',"Q19"],['d',"Q5"]],"Q4")
estadoA17=estado([['a',"Q6"],['b',"Q7"],['c',"Q7"],['d',"Q6"]],"Q17")
estadoA18=estado([['a',"Q7"],['b',"Q6"],['c',"Q7"],['d',"Q6"]],"Q18")
estadoA19=estado([['a',"Q7"],['b',"Q7"],['c',"Q6"],['d',"Q6"]],"Q19")

estadoA7=estado([['a',"Q7"],['b',"Q7"],['c',"Q7"],['d',"Q7"]],"Q7")
estadoA6=estado([['a',"Q7"],['b',"Q7"],['c',"Q7"],['d',"Q7"]],"Q6")
estadoA5=estado([['a',"Q6"],['b',"Q6"],['c',"Q6"],['d',"Q6"]],"Q5")


lstEstados=[]
lstEstados2=[]
lstEstados3=[]

lstEstados.append(estado0)
lstEstados.append(estado1)
lstEstados.append(estado2)
lstEstados.append(estado3)
lstEstados.append(estado4)
lstEstados.append(estado5)
lstEstados.append(estado6)

lstEstados2.append(estadoA0)
lstEstados2.append(estadoA1)
lstEstados2.append(estadoA2)
lstEstados2.append(estadoA3)
lstEstados2.append(estadoA4)
lstEstados2.append(estadoA5)
lstEstados2.append(estadoA6)
lstEstados2.append(estadoA7)
lstEstados2.append(estadoA8)
lstEstados2.append(estadoA9)
lstEstados2.append(estadoA10)
lstEstados2.append(estadoA11)
lstEstados2.append(estadoA12)
lstEstados2.append(estadoA13)
lstEstados2.append(estadoA14)
lstEstados2.append(estadoA15)
lstEstados2.append(estadoA16)
lstEstados2.append(estadoA17)
lstEstados2.append(estadoA18)
lstEstados2.append(estadoA19)

lstEstados3.append(estadoD0)
lstEstados3.append(estadoD1)
lstEstados3.append(estadoD2)
lstEstados3.append(estadoD3)
lstEstados3.append(estadoD4)
lstEstados3.append(estadoD5)
lstEstados3.append(estadoD6)
lstEstados3.append(estadoD7)
lstEstados3.append(estadoD8)

automata01=automata(lstEstados)
automata02=automata(lstEstados2)
automata03=automata(lstEstados3)

lstAceptados=[]
lstAceptados2=[]
lstAceptados3=[]

lstAceptados.append("Q2")
lstAceptados.append("Q6")

lstAceptados2.append("Q6")

lstAceptados3.append("Q6")
lstAceptados3.append("Q7")

while 1==1:
    cadena3=input("Escribe un numero real: ")

    for car in cadena3:
        automata03.transicion(car)

    if automata03.estadoNombre in lstAceptados3:
        print("cadena valida") 
        break
    else:
        print("Tu cadena es invalida")
        automata03=automata(lstEstados3)

while 1==1:
    cadena=input("Escribe una cadena con pares y sin 1 consecutivos: ")

    for car in cadena:
        automata01.transicion(int(car))


    if automata01.estadoNombre in lstAceptados:
        print("cadena valida") 
        break
    else:
        print("Tu cadena es invalida")
        automata01=automata(lstEstados)

while 1==1:
    cadena2=input("Escribe una cadena con a,b,c o d que almenos tenga 2 elementos repetidos y de longitud 3: ")

    for car in cadena2:
        automata02.transicion(car)

    if automata02.estadoNombre in lstAceptados2:
        print("cadena valida") 
        break

    else:
        print("Tu cadena es invalida")
        automata02=automata(lstEstados2)
        

