import re 
regexMail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexCURP = '^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'

regexIP="^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
regexURL = '^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?'



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
    
def checkURL(URL):
    if(re.match(regexURL,URL)):
        print("\n## URL Valido")
    else:
        print("\n## URL No valido")

def checkIP(IP):
    if(re.match(regexIP,IP)):
        print("\n## IP Valido")
    else:
        print("\n## IP No valido")

 
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
        [3] Validar IP
        [4] Validar URL
        [5] Salir
        
    """)
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        email_value = str(input("Escriba algun EMAIL para validar == "))
        checkCorreo(email_value)
    elif opcion == 2:
        curp_value = str(input("Escriba algun CURP para validar == "))
        checkCURP(curp_value)
    elif opcion == 3:
        ip_value = str(input("Escriba algun IP para validar == "))
        checkIP(ip_value)
    elif opcion == 4:
        url_value = str(input("Escriba el URL que desea verificar == "))
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")