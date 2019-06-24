import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from PrincipalController import ControllerPrincipal
from loginModel import LoginModel
from Inicio import Login
import ErrorUsuarioController
class Controllerlogin():

    def validarUsuario(self):
        modelo = LoginModel()
        lo = Login()
        datos = lo.Motrar()
        if not datos['user'] or not datos['pass']:
            err=ErrorUsuarioController.ErrorUsuario()
            err.erroCamVacios()
        else:
            validacion = modelo.validarUsuarioModel(datos['user'], datos['pass'])
            if (validacion == True):
                pri=ControllerPrincipal()
                pri.levantarVentanaCalculo()
            else:
                err=ErrorUsuarioController.ErrorUsuario()
                err.errorUIncorrecto()
                    

if __name__=="__main__":
    lo=Controllerlogin()
    lo.validarUsuario()