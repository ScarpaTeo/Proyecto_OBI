import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from PrincipalController import PrincipalController
from loginModel import LoginModel
from Inicio import Login
#from ErrorUsController import ErrorCntrl
from Error_Usuario import ErrorUsuario

class ErrorCntrl:
    def __init__(self):
        self.t = None
        self.Obtner()
        self.llamaralLogin()

    def Obtner(self):
        x = ErrorUsuario()
        x.mostrar()
        self.t = x.valor
        return self.t

    def llamaralLogin(self):
        if self.t == True:
            x = loginController()
            x.validarUsuario()

class loginController():

    def validarUsuario(self):
        modelo = LoginModel()
        lo = Login()
        datos = lo.Motrar()
        validacion = modelo.validarUsuarioModel(datos['user'], datos['pass'])
        if (validacion == True):
            pri=PrincipalController()
            pri.levantarVentanaCalculo()
        else:
            y = ErrorCntrl()



x = loginController()
x.validarUsuario()