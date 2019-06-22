import sys
sys.path.append('../vista')
from calculoCimiento import Cimiento
class Controllercalculo():
    
    def verCimiento(self):
        ci=Cimiento()
        dato=ci.vistaCimiento()
        
        #vuelve atras
        if dato==True:
            #se tiene que levantar la clase principal
            pass
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos de la DB
            #realizar los calculos 
            #ci.cargarResultado(resultado) // se le pasa el resultado de nuevo a la ventana
            pass