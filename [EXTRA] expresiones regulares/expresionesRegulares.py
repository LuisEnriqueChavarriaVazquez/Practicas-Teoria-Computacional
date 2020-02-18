from tkinter import messagebox
import re 
import sys
#from PyQt5 import QtCore, QtGui, QtWidgets, uic
#from windowProyectoExpresiones import Ui_MainWindow 

regexMail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regexCURP = '^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'
regexIP="^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

## ^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?
## extra
regexURL = '(^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[a-fA-F][a-fA-F]))+)$'



def checkCorreo(correo):
    if(re.match(regexMail,correo)):
        mensaje("\n### Correo Valido")
    else:
        mensaje("\n### Correo Invalido")

def checkCURP(CURP):
    if(re.match(regexCURP,CURP)):
        mensaje("\n### CURP Valido")
    else:
        mensaje("\n### CURP Invalido")
    
def checkURL(URL):
    if(re.match(regexURL,URL)):
        mensaje("\n## URL Valido")
    else:
        mensaje("\n## URL No valido")

def checkIP(IP):
    if(re.match(regexIP,IP)):
        mensaje("\n## IP Valido")
    else:
        mensaje("\n## IP No valido")

def mensaje(mensaje_value):
    messagebox.showinfo(message=mensaje_value, title="Validacion")

 
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
        checkURL(url_value)
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")


#######Prototipo de interfaz anterior
"""class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())"""