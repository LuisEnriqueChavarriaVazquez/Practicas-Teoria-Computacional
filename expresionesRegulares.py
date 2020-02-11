import re 
regexMail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexCURP = '^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'
regexRFC ='^([A-Z]{4}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01]))'#No esta completa tenog dudas con la homoclave del RFC

def checkCorreo(correo):
    if(re.match(regexMail,correo)):
        print("Correo Valido")
    else:
        print("Correo Invalido")

def checkCURP(CURP):
    if(re.match(regexCURP,CURP)):
        print("CURP Valido")
    else:
        print("CURP Invalido")

def checkRFC(RFC):
    if(re.match(regexRFC,RFC)):
        print("RFC Valido")
    else:
        print("RFC Invalido")

