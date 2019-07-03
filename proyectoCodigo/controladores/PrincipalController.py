import sys
sys.path.append('../modelos')
sys.path.append('../vista')
from Principal import Principal
import calculosController
class ControllerPrincipal():

    def __del__(self):
        print("objeto eliminado")

    #levanta las vistas de cada calculo
    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        ca=calculosController.Controllercalculo()
        if tipo=="cimiento":
            ca.verCimiento()
            sys.exit()
        elif tipo=="revoque":
            ca.verRevoque()
            sys.exit()
        elif tipo=="contrapiso":
            ca.verContrapiso()
            sys.exit()
        elif tipo=="pared":
            ca.verPared()
            sys.exit()
        elif tipo=="techo":
            ca.verTecho()
            sys.exit()

        
