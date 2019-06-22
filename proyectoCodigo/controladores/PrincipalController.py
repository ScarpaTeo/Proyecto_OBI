import sys
sys.path.append('../modelos')
sys.path.append('../vista')
from Principal import Principal
from calculosController import Controllercalculo
class ControllerPrincipal():

    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        ca=Controllercalculo()
        if tipo=="cimiento":
            ca.verCimiento()
        
        