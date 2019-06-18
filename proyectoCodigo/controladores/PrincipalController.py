import sys
sys.path.append('../modelos')
sys.path.append('../vista')
from Principal import Principal
from calculo import *

class PrincipalController():
    def levantarVentanaCalculo():
        pri=Principal()
        tipo=pri.mostrar()
        
        