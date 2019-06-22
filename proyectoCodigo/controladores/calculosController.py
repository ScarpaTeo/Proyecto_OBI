import sys
sys.path.append('../vista')
from PrincipalController import PrincipalController
class calculoController():
    
    
    def verCimiento(self):
        dato=self.ca.cimiento()
        #vuelve atras
        if dato==True:
            pri=PrincipalController()
            pri.levantarVentanaCalculo()
        #trae los datos para calcular
        if dato!=False and dato!=True:
            #traer datos del modelo
            #egregar funcion calculo