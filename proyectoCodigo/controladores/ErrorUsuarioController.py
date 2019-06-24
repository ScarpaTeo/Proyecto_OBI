import sys
sys.path.append('../vista')
sys.path.append('../modelos')
import loginController
from Error_Usuario import Error_Usuario

class ErrorUsuario():

    def erroCamVacios(self):
        er=Error_Usuario()
        dato=er.errorCamposVacios()
        if dato=="cerrar":
            lo=loginController.Controllerlogin()
            lo.validarUsuario()
    
    def errorUIncorrecto(self):
        err=Error_Usuario()
        dato=err.errorUsarioIncorrecto()
        if dato=="cerrar":
            lo=loginController.Controllerlogin()
            lo.validarUsuario()
