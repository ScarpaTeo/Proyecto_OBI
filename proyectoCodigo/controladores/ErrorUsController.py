import sys
sys.path.append('../vista')
sys.path.append('../modelos')
from loginController import loginController
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
        while self.t:
            x = loginController()
            x.validarUsuario()


#y= ErrorCntrl()