import re 
regexMail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexCURP = '^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'
regexRFC ='^([A-Z]{4}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01]))'#No esta completa tenog dudas con la homoclave del RFC
regexURL ##Voy a agregar la validacion de una URL con expresiones regulares para que halla un extra.



def checkCorreo(correo):
    if(re.match(regexMail,correo)):
        print("\n### Correo Valido")
    else:
        print("\n### Correo Invalido")

def checkCURP(CURP):
    if(re.match(regexCURP,CURP)):
        print("\n### CURP Valido")
    else:
        print("\n### CURP Invalido")

def checkRFC(RFC):
    if(re.match(regexRFC,RFC)):
        print("\n### RFC Valido")
    else:
        print("\n### RFC Invalido")

 
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce alguna opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print("""

/// Bienvenido al validador de expresiones regulares!!!
        
        Seleccione alguna opcion:
        [1] Validar EMAIL
        [2] Validar CURP
        [3] Validar RFC
        [4] Salir
        
    """)
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        email_value = str(input("Escriba algun EMAIL para validar == "))
        checkCorreo(email_value)
    elif opcion == 2:
        curp_value = str(input("Escriba algun CURP para validar == "))
        checkCURP(curp_value)
    elif opcion == 3:
        rfc_value = str(input("Escriba algun RFC para validar == "))
        checkRFC(rfc_value)
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    
