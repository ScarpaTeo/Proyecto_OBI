import sys
sys.path.append('../modelos')
sys.path.append('../vista')
from Principal import Principal
import calculosController
class ControllerPrincipal():

    #levanta las vistas de cada calculo
    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        ca=calculosController.Controllercalculo()
        if tipo=="cimiento":
            ca.verCimiento()
        elif tipo=="revoque":
            ca.verRevoque()
        elif tipo=="contrapiso":
            ca.verContrapiso()
        elif tipo=="pared":
            ca.verPared()
        elif tipo=="techo":
            ca.verTecho()
        
        