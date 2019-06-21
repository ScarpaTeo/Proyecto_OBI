import sys
sys.path.append('../modelos')
sys.path.append('../vista')
from Principal import Principal
from calculo import *

class PrincipalController():
    def levantarVentanaCalculo(self):
        pri=Principal()
        tipo=pri.mostrar()
        ca=calculo()
        if tipo=="cimiento":
            ca.cimiento()
        elif tipo=="pared":
            ca.pared()
        elif tipo=="contrapiso":
            ca.cimiento()
        elif tipo=="revoque":
            ca.revoque()
        elif tipo=="techo":
            ca.techo()
    
        
        