import sys
sys.path.append('../vista')
from Error_Calculo import Error_Calculo
class ControllerCalculoError():

    def campoVacio(self):
        err=Error_Calculo()
        dato=err.errorCamposVacios()
        return dato
    def campoIncorrecto(self):
        err=Error_Calculo()
        dato=err.errorValoresIncorrectos()
        return dato


